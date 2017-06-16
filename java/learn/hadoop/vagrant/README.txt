# vagrant 使用说明
https://www.vagrantup.com/docs/virtualbox/boxes.html

# 虚拟机
# 安装guest additions
sudo apt-get install linux-headers-$(uname -r) build-essential dkms
sudo mount /dev/cdrom /media/cdrom
sudo sh /media/cdrom/VBoxLinuxAdditions.run

# 配置sudo免密权限
# vi /etc/sudoers
# lidong	ALL=(ALL:ALL) NOPASSWD:ALL
# %lidong	ALL=(ALL:ALL) NOPASSWD:ALL

# 配置一个NAT网络(vagrant)， 一个桥接网络

# Host机, 从VirtualBox导出
# vagrant package --base vbox-name (hadoop)
# vagrant box add hadoop /path/to/the/new.box
# vagrant box list
# 只有在没有Vagrantfile文件时执行vagrant init
# vagrant init hadoop (在当前路径下生成Vagrantfile文件)
# 配置好Vagrantfile启动虚拟机
# vagrant up
# 登录
# vagrant ssh

# vm重启，但是不清除已写入vm中数据
# vagrant reload
# 删除虚拟机
# vagrant destroy
# vagrant suspend
# vagrant resume
# 关机
# vagrant halt

# 打包当前配置
# vagrant package --output backup.box

# 多台集群启动
# http://kiwenlau.com/2016/07/03/vagrant-vm-cluster/
# 启动多个
# vagrant up
# 启动1个
# vagrant up node1
# 启动2个
# vagrant up node1 node2

# 显示状态
vagrant status [node1|node2|node3]

# 重启并执行provision （比如 shell）
# vagrant reload --provision

# 启动执行provision， 当需要重新需要在vm机执行脚本时，很方便
# vagrant up --provision node1

# 环境变量：
# 修改配置文件的名字
# VAGRANT_VAGRANTFILE 
# 找一个大的硬盘存放
# export VAGRANT_DOTFILE_PATH = /system/vagrant
