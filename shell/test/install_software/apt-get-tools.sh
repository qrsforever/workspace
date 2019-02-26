#!/bin/bash

sudo apt-get install -y ssh tree ascii

sudo apt-get install -y gnome-core fcitx-bin fcitx-table gnome-tweak-tool

sudo apt-get install -y git vim vim-gtk terminator chromium-browser goldendict curl npm

sudo apt-get install -y xclip ctags cscope cmake cmake-curses-gui pkg-config scons

sudo apt-get install -y python3-pip

# color拾取
cd /tmp
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcolor2/gcolor2_0.4-2.1ubuntu1_amd64.deb
sudo apt-get install ./gcolor2_0.4-2.1ubuntu1_amd64.deb
cd -
