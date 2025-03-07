#!/bin/sh

docker logs --since 24h steam-game-remover -t | less +G
