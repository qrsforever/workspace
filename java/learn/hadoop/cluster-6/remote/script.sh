#!/bin/bash

###### 系统设置 ######
WS_DIR=/home/lidong/workspace
if [[ ! -d $WS_DIR ]]
then
    mkdir -p $WS_DIR
    chown lidong:lidong $WS_DIR
fi

COMMON_NFS=/home/lidong/nfs/common

# 关闭防火强
ufw disable

# 更改/etc/配置
if [[ -d $COMMON_NFS/linux/etc/ ]]
then
    cp $COMMON_NFS/linux/etc/* /etc
fi

###### Hadoop配置 ######

HADOOP_HOME=/data/opt/hadoop/hadoop-2.8.0
HADOOP_NFS=/home/lidong/nfs/hadoop

__do_hadoop() {
    cd $HADOOP_HOME

    if [[ ! -f etc.tar.gz ]]
    then
        tar zcf etc.tar.gz etc
    fi
    rm -rf logs
    rm -rf etc
    tar zxf etc.tar.gz 

    if [[ ! -d $WS_DIR/hadoop ]]
    then
        mkdir -p $WS_DIR/hadoop/tmp
        mkdir -p $WS_DIR/hadoop/logs
        chown -R lidong:lidong $WS_DIR/hadoop
    fi

    # 先copy公共配置
    if [[ -d $COMMON_NFS/hadoop/etc ]]
    then
        cp -arpf $COMMON_NFS/hadoop/etc/* etc/hadoop
    fi

    # 在copy差异配置
    if [[ -d $HADOOP_NFS/etc ]]
    then
        cp -arpf $HADOOP_NFS/etc/* etc/hadoop
    fi


    cd -
}

###### Zookeeper配置 ######

ZOOKEEPER_HOME=/data/opt/zookeeper/zookeeper-3.4.10
ZOOKEEPER_NFS=/home/lidong/nfs/zookeeper
ZOOKEEPER_TDIR=$WS_DIR/zookeeper

cd $ZOOKEEPER_HOME

__do_zookeeper() {
    if [[ ! -f conf.tar.gz ]]
    then
        tar zcf conf.tar.gz conf
    fi
    rm -rf conf
    tar zxf conf.tar.gz 

    if [[ ! -d $WS_DIR/zookeeper ]]
    then
        mkdir -p $WS_DIR/zookeeper/data
        mkdir -p $WS_DIR/zookeeper/logs
        chown -R lidong:lidong $WS_DIR/zookeeper
    fi
    myid=`echo $1 | cut -c5-`
    myid=`expr $myid - 2`
    echo "$myid" > $WS_DIR/zookeeper/data/myid

    # 先copy公共配置
    if [[ -d $COMMON_NFS/zookeeper/conf ]]
    then
        cp -aprf $COMMON_NFS/zookeeper/conf/* conf
    fi

    # 在copy差异配置
    if [[ -d $ZOOKEEPER_NFS/conf ]]
    then
        cp -aprf $ZOOKEEPER_NFS/conf/* conf
    fi

    cd -
}

hn=$1

__do_hadoop $hn

if [ $hn == "node3" -o $hn == "node4" -o $hn == "node5" ]
then
    __do_zookeeper $hn
    $ZOOKEEPER_HOME/bin/zkServer.sh restart
    $HADOOP_HOME/sbin/hadoop-daemon.sh stop journalnode
    $HADOOP_HOME/sbin/hadoop-daemon.sh start journalnode
fi
