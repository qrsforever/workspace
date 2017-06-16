#!/bin/bash

###### 系统设置 ######
TMP_DIR=/home/lidong/tmp
if [[ ! -d $TMP_DIR ]]
then
    mkdir -p $TMP_DIR
    chown lidong:lidong $TMP_DIR
fi

COMMON_DIR=/home/lidong/common

# 关闭防火强
ufw disable

# 设置hosts
echo "127.0.0.1 localhost" > /etc/hosts
echo "127.0.0.1 vbox" >> /etc/hosts

echo "::1     localhost ip6-localhost ip6-loopback" >> /etc/hosts
echo "ff02::1 ip6-allnodes" >> /etc/hosts
echo "ff02::2 ip6-allrouters" >> /etc/hosts

echo "192.168.1.102   master">> /etc/hosts
echo "192.168.1.201   node1" >> /etc/hosts
echo "192.168.1.202   node2" >> /etc/hosts
echo "192.168.1.203   node3" >> /etc/hosts
echo "192.168.1.204   node4" >> /etc/hosts
echo "192.168.1.205   node5" >> /etc/hosts
echo "192.168.1.206   node6" >> /etc/hosts

###### Hadoop配置 ######

HADOOP_HOME=/data/opt/hadoop/hadoop-2.8.0
HADOOP_MOUNT=/home/lidong/hadoop

cd $HADOOP_HOME

if [[ ! -f etc.tar.gz ]]
then
    tar zcf etc.tar.gz etc
fi
rm -rf logs
rm -rf etc
tar zxf etc.tar.gz 

# 先copy公共配置
if [[ -d $COMMON_DIR/hadoop/etc ]]
then
    cp -arpf $COMMON_DIR/hadoop/etc/* etc/hadoop
fi

# 在copy差异配置
if [[ -d $HADOOP_MOUNT/etc ]]
then
    cp -arpf $HADOOP_MOUNT/etc/* etc/hadoop
fi

cd -

###### Zookeeper配置 ######

ZOOKEEPER_HOME=/data/opt/zookeeper/zookeeper-3.4.10
ZOOKEEPER_MOUNT=/home/lidong/zookeeper
ZOOKEEPER_TDIR=$TMP_DIR/zookeeper

cd $ZOOKEEPER_HOME

if [[ ! -f conf.tar.gz ]]
then
    tar zcf conf.tar.gz conf
fi
rm -rf conf
tar zxf conf.tar.gz 

if [[ ! -d $ZOOKEEPER_TDIR ]]
then
    mkdir -p $ZOOKEEPER_TDIR/data
    mkdir -p $ZOOKEEPER_TDIR/logs
    chown -R lidong:lidong $ZOOKEEPER_TDIR
fi
myid=`hostname | cut -c5-`
myid=`expr $myid - 2`
echo "$myid" > $ZOOKEEPER_TDIR/data/myid

echo "#!/usr/bin/env bash" > conf/zookeeper-env.sh
echo "ZOO_LOG_DIR=$ZOOKEEPER_TDIR/logs" >> conf/zookeeper-env.sh

# 先copy公共配置
if [[ -d $COMMON_DIR/zookeeper/conf ]]
then
    cp -aprf $COMMON_DIR/zookeeper/conf/* conf
fi

# 在copy差异配置
if [[ -d $ZOOKEEPER_MOUNT/conf ]]
then
    cp -aprf $ZOOKEEPER_MOUNT/conf/* conf
fi

cd -
