#!/bin/bash

if [[ x"$HBASE_HOME" == x ]]
then
    echo "Please set: export HBASE_HOME"
    exit 0
fi

current_dir=`pwd`
replace_dir=$current_dir/__replace__

# 配置备份，还原
cd $HBASE_HOME

if [[ ! -f conf.tar.gz ]]
then
    tar zcf conf.tar.gz conf
fi

rm -rf conf
tar zxf conf.tar.gz
if [[ -d $replace_dir/hbase/conf ]]
then
    cp -aprf $replace_dir/hbase/conf/* conf/
fi

cd -

# 启动hbase
start-hbase.sh

# jps

# HBase： Row Key, 列族， 列标识， Cell
# hbase shell
# ============================== HBASE SHELL ===============
# help
# create 'test', 'data'
# list
# put 'test', 'row1', 'data:1', 'value1'
# get 'test', 'row1'
# scan 'test'
# count 'test'
# disable 'test'
# drop 'test'
# list
# quit
# ============================== HBASE SHELL ===============

# mvn package
# HBASE_CLASSPATH=target/learn-hbase-1.0.0.jar 
# hbase com.java.learn.ExampleClient

# 停止hbase
# stop-hbase.sh

# 打开api web
echo "google-chrome file://$HBASE_HOME/docs/apidocs/index.html"
echo "google-chrome file://$HADOOP_HOME/share/doc/hadoop/api/index.html"
