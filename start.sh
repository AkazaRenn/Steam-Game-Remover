#!/bin/sh

CONTAINER_NAME="steam-game-remover"
TAG=$(curl -s https://mcr.microsoft.com/v2/playwright/python/tags/list | jq -r '.tags | .[]' | sort -rV | grep jammy-amd64 | head -n 1)
IMAGE="mcr.microsoft.com/playwright/python:${TAG}"

docker pull ${IMAGE}
docker rm -f ${CONTAINER_NAME} &> /dev/null
docker run -d --name ${CONTAINER_NAME} --restart unless-stopped -v $(pwd):$(pwd) -w $(pwd) --entrypoint $(pwd)/entrypoint.sh ${IMAGE}
