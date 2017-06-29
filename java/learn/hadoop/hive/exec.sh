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
fi

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

# mysql创建/删除数据库 (initSchema 会自动创建)
# mysql -uroot -p123456 -h localhost -e "create database hive"
# 如果mysql方式有问题， 需要删除hive数据库，重新初始化
mysql -uroot -p123456 -h localhost -e "drop database if exists hive"

# derby：单实例， 不能存在多个hive实例
# 初始化数据库
schematool -initSchema -dbType $dtype
# 查看初始化结果
schematool -info -dbType $dtype

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

# learn-4
# hive> show functions
# hive> describe function sum

# learn-5
rm tmp -rf
mkdir tmp
echo "3105007001,192.168.1.1" >  tmp/login.txt 
echo "3105007002,192.168.1.2" >> tmp/login.txt 
echo "3105007003,192.168.1.3" >  tmp/login2.txt 
echo "3105007004,192.168.1.4" >> tmp/login2.txt 
# hive -f src/main/hive/partition.sql

echo "192.168.1.1,3105007001|3105007002|3105007003" >  tmp/login_array.txt 
echo "192.168.1.2,3105007004|3105007005" >> tmp/login_array.txt 

echo "192.168.1.1,aa:11|bb:22|cc:33" >  tmp/login_map.txt
echo "192.168.1.2,aa:11|bb:22" >> tmp/login_map.txt

echo "192.168.1.1,user1:0001" >  tmp/login_struct.txt
echo "192.168.1.2,user2:0002" >> tmp/login_struct.txt

echo "192.168.1.1,user1:0001|user2:0002|user3:0003" >  tmp/login_complex.txt
echo "192.168.1.2,user1:0001" >> tmp/login_complex.txt
# hive -f src/main/hive/complex.sql
