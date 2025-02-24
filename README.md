# Steam Game Remover
Remove your free Steam games added by the SteamDB tool from a headless server.

## Instruction
### Get cookies
1. Install [`cookies.txt` add-on](https://github.com/hrdl-github/cookies-txt) to your browser
2. Make sure you are loggin at https://store.steampowered.com, get your `cookies.txt` using the add-on
3. Transfer `cookies.txt` to the server, place it in the same dir of the project
4. Run `convert_cookie.py`, it generates `cookies.json`, now you can delete `cookies.txt`
### Start container
1. Make sure you have `Docker` installed, adjust the scripts accordingly if you are using `Podman`
2. Run `start.sh`, it should be able to handle the rest
3. Run `logs.sh` to check the results

## Limitations
Removing free games is limited to once in every 10 minutes once you have removed 10 games.
