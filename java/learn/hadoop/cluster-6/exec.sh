#!/bin/bash

# 参考
# http://blog.csdn.net/uq_jin/article/details/51487439

# master: /etc/hosts
# 192.168.1.102     master
# 192.168.1.201     node1
# 192.168.1.202     node2
# 192.168.1.203     node3
# 192.168.1.204     node4
# 192.168.1.205     node5
# 192.168.1.206     node6

echo "export VAGRANT_DOTFILE_PATH=/system/vagrant" 
echo "vagrant up node1 node2 node3 node4 node5"

export HADOOP_HOME=/data/opt/hadoop/hadoop-2.8.0
export REMOTE_DIR=$PWD/remote

cd $HADOOP_HOME

if [[ ! -f etc.tar.gz ]]
then
    tar zcf etc.tar.gz etc
fi
rm -rf etc
rm -rf logs
tar zxvf etc.tar.gz

cp -aprf $REMOTE_DIR/common/hadoop/etc/* etc/hadoop

cd -
