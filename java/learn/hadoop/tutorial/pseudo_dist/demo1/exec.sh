#!/bin/bash

# First: cd setup ;  ./script.sh

if [[ x$HADOOP_HOME == x ]]
then
    echo "not set HADOOP_HOME envirnment"
    exit 0
fi

if [[ -d ~/workspace/hadoop/tmp ]]
then
    rm ~/workspace/hadoop/tmp -rf
fi

if [[ -d ~/workspace/hadoop/logs ]]
then
    rm ~/workspace/hadoop/logs -rf
fi

__start()
{
    $HADOOP_HOME/bin/hdfs namenode -format -force -nonInteractive

    # Start NameNode daemon and DataNode daemon
    $HADOOP_HOME/sbin/start-dfs.sh 

    # 命令相同: hadoop fs -mkdir == hdfs dfs -mkdir 
    $HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/$USER
    $HADOOP_HOME/bin/hdfs dfs -chmod g+w /user/$USER
    $HADOOP_HOME/bin/hdfs dfs -ls /

    # 浏览namenode: http://localhost:50070/

    # hdfs dfs 所有命令的相对路径是 /user/$USER
    # hdfs://localhost:9000/user/$USER/input
    $HADOOP_HOME/bin/hdfs dfs -put $HADOOP_HOME/etc/hadoop input
    $HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-${HADOOP_VERSION}.jar \
        grep input output 'dfs[a-z.]+'

    # 使用绝对路径
    $HADOOP_HOME/bin/hdfs dfs -cat /user/$USER/output/*

    # 使用工作路径
    $HADOOP_HOME/bin/hdfs dfs -cat output/*
    $HADOOP_HOME/bin/hdfs dfs -get output

    $HADOOP_HOME/sbin/stop-dfs.sh
}

__start
