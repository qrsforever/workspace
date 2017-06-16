#!/bin/bash

HADOOP_HOME=/data/opt/hadoop/hadoop-2.8.0

ret=`cat /etc/hosts | grep master`

if [[ x$ret == x ]]
then
    echo "192.168.1.102   master">> /etc/hosts
    echo "192.168.1.201   node1" >> /etc/hosts
    echo "192.168.1.202   node2" >> /etc/hosts
    echo "192.168.1.203   node3" >> /etc/hosts
    echo "192.168.1.204   node4" >> /etc/hosts
    echo "192.168.1.205   node5" >> /etc/hosts
    echo "192.168.1.206   node6" >> /etc/hosts
fi

cd $HADOOP_HOME

if [[ ! -f etc.tar.gz ]]
then
    tar zcf etc.tar.gz etc
fi
tar zxf etc.tar.gz 
cp -arpf /home/lidong/hadoop/etc/* etc/hadoop

cd -
