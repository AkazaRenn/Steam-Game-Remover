from playwright.sync_api import sync_playwright
import json, re, time

def main():
    try:
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
    except:
        pass

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        context.add_cookies(cookies)

        page = context.new_page()

        while True:
            try:
                page.goto("https://store.steampowered.com/login/")
                page.wait_for_url("https://store.steampowered.com/")

                cookies = page.context.cookies()
                with open("cookies.json", "w") as f:
                    json.dump(cookies, f, indent=4)

                page.goto("https://store.steampowered.com/account/licenses/")
                html_content = page.content()
                package_ids = re.findall(r'javascript:RemoveFreeLicense\( (\d+),', html_content)
                package_count = len(package_ids)
                print(f"Extracted {package_count} package IDs")
                if package_count <= 0:
                    print(f"Nothing to remove\n{html_content}")
                    exit(0)

                session_id = ''
                for cookie in cookies:
                    if cookie["name"] == "sessionid":  # Replace with the actual name of the session ID cookie
                        session_id = cookie["value"]
                        break

                for i in range(20):
                    package_id = package_ids[i]
                    js_code = f"""
                        (async () => {{
                            const response = await fetch('https://store.steampowered.com/account/removelicense', {{
                                method: 'POST',
                                headers: {{
                                    'Content-Type': 'application/x-www-form-urlencoded'
                                }},
                                body: `sessionid={session_id}&packageid={package_id}`
                            }});

                            const result = await response.json(); // Convert response to JSON
                            return result;
                        }})();
                        """

                    while True:
                        result = page.evaluate(js_code)
                        if result.get('success') == 1:
                            package_count -= 1
                            print(f'Successfully removed game ID {package_id}, remaining {package_count}')
                            break
                        time.sleep(600)
            except Exception as e:
                print(f"Error: {e}")

        browser.close()


if __name__ == "__main__":
    main()
