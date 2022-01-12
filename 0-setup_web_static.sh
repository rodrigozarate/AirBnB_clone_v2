#!/usr/bin/env bash
# Example of script to configure a server
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y nginx
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
echo "<h1>AirBnB</h1>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown unubtu:ubuntu -hR /data/
sudo service nginx restart
