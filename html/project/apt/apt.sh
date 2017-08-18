#!/bin/bash

# nodejs https://nodejs.org/en/
curl -sL https://deb.nodesource.com/setup_6.x | /usr/bin/sudo -E bash -
sudo apt-get  install nodejs

# hexo
sudo npm install -g hexo-cli
