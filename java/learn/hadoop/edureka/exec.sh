#!/bin/bash

# https://www.edureka.co/blog/setting-up-a-multi-node-cluster-in-hadoop-2.X

# 关闭防火墙
# sudo iptables -P INPUT ACCEPT
# sudo iptables -P OUTPUT ACCEPT

# selinux: /etc/selinux/config
# SELINUX=permissive

# hadoop的安装路径也必须一致
# master 和 slave 的用户名必须一致， hadoop代码中无法修改
# sudo useradd -m lidong8 -s /bin/bash
# sudo passwd lidong8 # passwd:1

# 设置master node1 hosts
# /etc/hosts
# 192.168.1.102  	master
# 192.168.1.201  	node1

# node1: cat /etc/network/interfaces
# iface enp0s3 inet static
# address 192.168.1.201
# gateway 192.168.1.1
# netmask 255.255.255.0
# network 192.168.1.0
# broadcast 192.168.1.255

# ssh-keygen -t rsa -P ""
# cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
# ssh-copy-id -i $HOME/.ssh/id_rsa.pub lidong8@192.168.1.201 or (node1)

echo -e "\n"

#废除(配置remote),  使用vagrant搭建智能环境
# echo "ssh node1 'mkdir -p ~/hadoop/edureka/etc/' "
# echo "scp etc/remote/* node1:~/hadoop/edureka/etc"
# echo "scp ../pre-start.sh node1:~/hadoop"
# echo "scp ../post-stop.sh node1:~/hadoop"

# 本机上所有的vm机到install在/system/vagrant, 多个工程共享
echo "export VAGRANT_DOTFILE_PATH=/system/vagrant"
echo "vagrant up node1"

echo -e "\n"
echo "../pre-start.sh"
echo -e "\n"

echo "$HADOOP_HOME/bin/hadoop namenode -format"
echo "$HADOOP_HOME/sbin/start-dfs.sh"
echo "$HADOOP_HOME/sbin/start-yarn.sh"
echo "google-chrome http://master:50070/dfshealth.html"

echo -e "\n"

echo "$HADOOP_HOME/sbin/stop-dfs.sh"
echo "$HADOOP_HOME/sbin/stop-yarn.sh"
echo "vagrant halt node1"

echo -e "\n"
echo "../post-stop.sh"
