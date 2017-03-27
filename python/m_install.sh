#!/bin/bash

sudo apt-get install python

# 基础开发环境
sudo apt-get install python-dev

# 管理工具
sudo apt-get install python-pip

# 增强Shell
sudo apt-get install ipython
sudo pip install wcwidth
sudo pip install ptyprocess

# 安装Notebook以及依赖库:tornado 和 pyzmq.
sudo apt-get install ipython-notebook 
sudo pip install tornado
sudo apt-get install libzmq-dev
sudo pip install pyzmq
sudo pip install pygments

# 科学计算相关库(矩阵，数值计算， 绘图)
sudo apt-get install python-numpy
sudo apt-get install python-scipy
sudo apt-get install python-matplotlib

# 使用pip编译安装时， 检查依赖, 更新
sudo apt-get build-dep python-numpy
sudo apt-get build-dep python-scipy
sudo pip install numpy
sudo pip install scipy

# Qt设计器
sudo apt-get install python-qt4
sudo apt-get install qt4-designer
sudo apt-get install pyqt4-dev-tools
sudo apt-get install python-qt4-doc

# 安装简单IDE 
sudo apt-get install spyder
sudo pip install spyder --upgrade

# 扩展模块
sudo pip install cython
sudo apt-get install swig

# 数据分析
sudo apt-get python-pandas

# 工具套装ETS
sudo apt-get install libxtst-dev scons python-vtk pyqt4-dev-tools 
sudo apt-get install python2.7-wxgtk2.8 python-configobj
sudo apt-get install libgl1-mesa-dev libglu1-mesa-dev
rm -f /tmp/ets
mkdir /tmp/ets
cd /tmp/ets
git clone git@github.com:enthought/ets.git
cd ets
python ets.py clone
sudo python setup.py develop
cd -
cd -

# 图像处理和计算机视觉 (opencv)
sudo apt-get install harpia libcv2.4 libcvaux2.4 
sudo apt-get install libhighgui2.4 libcv-dev libcvaux-dev
sudo apt-get install libhighgui-dev opencv-doc python-opencv

# 测试库
sudo apt-get install python-nose
sudo apt-get install python-pytest

# Others
sudo pip install jedi --upgrade
sudo pip install tox pytest

# 代码规范 需要vpn
sudo pip install flake8

# sudo apt-get install python3-dev
# sudo apt-get install python3-pip
# sudo apt-get install python3-tk
# sudo pip3 install pylint flake8 pyflakes
