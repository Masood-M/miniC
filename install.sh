#!/bin/bash
# Exit immediately if a command exits with a non-zero status

sudo apt-get update

sudo apt-get install -y nano python nano make gcc autoconf automake libtool python-dev libpcre3-dev
sudo apt-get install clamav
sudo freshclam
