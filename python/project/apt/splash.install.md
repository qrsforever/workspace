https://splash.readthedocs.io/en/stable/install.html


# docker (推荐)

[docker安装](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

sudo pip3 install scrapy-splash

sudo docker pull scrapinghub/splash

docker run -it -p 8050:8050 scrapinghub/splash


# 手动

```

git clone https://github.com/scrapinghub/splash/

cd splash/dockerfiles/splash
sudo cp ./qt-installer-noninteractive.qs /tmp/script.qs
sudo ./provision.sh \
         prepare_install \
         install_msfonts \
         install_extra_fonts \
         install_deps \
         install_flash \
         install_qtwebkit_deps \
         install_official_qt \
         install_qtwebkit \
         install_pyqt5 \
         install_python_deps

```

