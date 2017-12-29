#!/usr/bin/env bash

USERNAME=pi
PASSWORD=raspberry

echo -en "Deploying..."
sshpass -p "$PASSWORD" rsync -avz ./ "$USERNAME"@raspi:/frontends/smarthome
echo -e "done!";

#Oneliner
# USERNAME=pi; PASSWORD=raspberry; sshpass -p "$PASSWORD" rsync -avz ./ "$USERNAME"@raspi:/frontends/smarthome