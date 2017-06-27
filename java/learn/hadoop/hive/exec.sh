#!/bin/bash

if [ x$HADOOP_HOME == x -o x$HIVE_HOME == x ]
then
    echo "not set HADOOP_HOME HIVE_HOME envirnment"
    exit 0
fi

# dbtype: derby|mysql|postgres|oracle|mssql 
dtype=mysql

if [[ x$1 != x ]]
then
    dtype=derby
if

cur_dir=`pwd`

cd $HADOOP_HOME

if [[ ! -f etc.tar.gz ]]
then
    tar zcf etc.tar.gz etc
fi

rm etc -rf
tar zxf etc.tar.gz
cp -aprf $cur_dir/__replace__/hadoop/etc/* etc/hadoop/

cd -

cd $HIVE_HOME

if [[ ! -f conf.tar.gz ]]
then
    tar zcf conf.tar.gz conf
fi

rm conf -rf
tar zxf conf.tar.gz
cp -aprf $cur_dir/__replace__/hive/$dtype/conf/* conf/

cd -

$HADOOP_HOME/bin/hdfs namenode -format -nonInteractive

$HADOOP_HOME/sbin/start-dfs.sh 
# $HADOOP_HOME/sbin/stop-dfs.sh 

# schema模式版本校验
echo "====================> dbtype: $dtype"
# derby：单实例， 不能存在多个hive实例
# 这个第一次必须执行
schematool -initSchema -dbType $dtype

# lean-1

# 从脚本文件执行
# hive -f script.q
# 从CMD字符串执行
# hive -e 'show tables'

# echo "X" > dummy.txt
# hive -e "create table dummy (value string); load data local inpath 'dummy.txt' overwrite into table dummy"
# -S 抑制错误信息输出
# hive -S -e 'select * from dummy'

# lean-2

# hive -f ./src/main/hive/records.hive
# 查看数据存放位置: hive.metastore.warehouse.dir
# hadoop fs -cat /user/lidong/warehouse/records/sample.txt

# learn-3 
# 列出属性 set -a 所有
# hive> set; 
# 查看单一个属性，如job引擎
# set hive.execution.engine;
