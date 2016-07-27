#!/bin/sh

## Remove unused packages
sudo apt-get autoremove

## Find removed packages that left their configuration behind, and remove them.
sudo dpkg -l | grep "^rc.*" | awk {'print $2'} | xargs sudo apt-get -y purge
