#!/bin/bash

__apt_install() {
    sudo apt-get -y install $*
}

__pip_install() {
    sudo pip install $*
    sudo pip3 install $*
}

__apt_install python python3

# 基础开发环境
__apt_install python-dev python3-dev

# 管理工具
__apt_install python-pip python3-pip

# 增强Shell
__apt_install ipython
sudo pip install wcwidth
sudo pip install ptyprocess

# 安装Notebook以及依赖库:tornado 和 pyzmq.
__apt_install ipython-notebook 
sudo pip install tornado
__apt_install libzmq-dev
sudo pip install pyzmq
sudo pip install pygments

# 科学计算相关库(矩阵，数值计算， 绘图)
__apt_install python-numpy python3-numpy
__apt_install python-scipy python3-scipy
__apt_install python-matplotlib python3-matplotlib

# 数据分析
__apt_install python-pandas python3-pandas

# 基本图形库
__apt_install python-tk python3-tk

# 使用pip编译安装时， 检查依赖, 更新
# sudo apt-get -y build-dep python-numpy
# sudo apt-get -y build-dep python-scipy
# sudo pip install numpy
# sudo pip install scipy

# Qt设计器
__apt_install python-qt4
__apt_install qt4-designer
__apt_install pyqt4-dev-tools
__apt_install python-qt4-doc

# 安装简单IDE 
__apt_install spyder
sudo pip install spyder --upgrade

# 扩展模块
sudo pip install cython
__apt_install swig

# 工具套装ETS
__apt_install libxtst-dev scons python-vtk pyqt4-dev-tools 
__apt_install python2.7-wxgtk2.8 python-configobj
__apt_install libgl1-mesa-dev libglu1-mesa-dev
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
__apt_install harpia libcv2.4 libcvaux2.4 
__apt_install libhighgui2.4 libcv-dev libcvaux-dev
__apt_install libhighgui-dev opencv-doc python-opencv

# 测试库
__apt_install python-nose
__apt_install python-pytest

# Others
sudo pip install jedi --upgrade
sudo pip install tox pytest

#==============================================================
#==============================================================
#==============================================================
#==============================================================
#==============================================================

#文本处理工具
__pip_install gensim

# 代码规范
__pip_install flake8 pylint pyflakes

#机器学习
__pip_install sklearn-pandas

# 分布式任务调度
__pip_install Celery

# avro 序列化反序列化
__pip_install avro
