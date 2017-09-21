#!/bin/bash

if [[ x$HADOOP_HOME == x ]]
then
    echo "not set HADOOP_HOME envirnment"
    exit 0
fi

current_dir=`pwd`

cd $HADOOP_HOME

# 备份
if [[ ! -f etc.tar.gz ]]
then
    tar zcf etc.tar.gz etc
fi
rm -rf logs
rm -rf etc
tar zxf etc.tar.gz 

cp $current_dir/hadoop/etc/* etc/hadoop

cd - 1 &>/dev/null
