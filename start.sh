#!/bin/sh

CONTAINER_NAME="steam-game-remover"

docker rm -f ${CONTAINER_NAME}
docker run -d --name ${CONTAINER_NAME} -v $(pwd):$(pwd) -w $(pwd) --entrypoint $(pwd)/entrypoint.sh mcr.microsoft.com/playwright/python:v1.50.0-jammy
