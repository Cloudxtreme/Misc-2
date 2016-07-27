#!/bin/bash

for line in $(sudo systemctl list-units --no-page -q | grep -i ".service" | grep -v "●" | awk {'print $1'}); do
    read -p "Kill and disable service: ($line)? [y/n]  " VAR
    if [ "$VAR" == "y" ]
    then
        sudo systemctl disable "$line" || \
        echo "Error disabling service" && \
        sudo systemctl stop "$line" && \
        echo "Service terminated and disabled." || \
        echo "Error terminating service"
    fi
done
