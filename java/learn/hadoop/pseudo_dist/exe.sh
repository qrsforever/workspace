#!/bin/bash

if [[ x$HADOOP_HOME == x ]]
then
    echo "not set HADOOP_HOME envirnment"
    exit 0
fi

cur_dir=`pwd`

cd $HADOOP_HOME

if [[ ! -f etc.tar.gz ]]
then
    tar zcf etc.tar.gz etc
fi

rm etc -rf
tar zxf etc.tar.gz
cp -aprf $cur_dir/etc/* etc/hadoop/

$HADOOP_HOME/bin/hdfs namenode -format -nonInteractive

# Start NameNode daemon and DataNode daemon
$HADOOP_HOME/sbin/start-dfs.sh 

# Test:
# 浏览namenode: http://localhost:50070/
# hdfs dfs -mkdir -p /user/$USER
# hdfs dfs -ls /

# hdfs dfs 所有命令的相对路径是 /user/$USER
# hdfs://localhost:9000/user/$USER/input
# hdfs dfs -put etc/ input
# hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.0.jar grep input output 'jdk[0-9._]+'
# 使用绝对路径
# hdfs dfs -cat /user/lidong8/output/*
# 使用工作路径
# hdfs dfs -cat output/*
# hdfs dfs -get output

$HADOOP_HOME/bin/hadoop fs -mkdir -p /tmp
$HADOOP_HOME/bin/hadoop fs -mkdir -p /user/$USER
$HADOOP_HOME/bin/hadoop fs -chmod g+w /tmp
$HADOOP_HOME/bin/hadoop fs -chmod g+w /user/$USER

# $HADOOP_HOME/sbin/stop-dfs.sh 
