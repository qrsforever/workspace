#!/bin/bash

# 生成pom.xml
# mvn archetype:generate
# 编译
# mvn package

# 从Hadoop URL中读取数据

arg=$1

if [[ x$arg == x1 ]]
then
    ../../../pre-start.sh
    hdfs namenode -format -nonInteractive
    start-dfs.sh 
    # 必须先创建一个用户， 相对路径就是/user/$USER
    hadoop fs -mkdir -p /user/$USER
    hadoop fs -copyFromLocal $0 $0
fi

if [[ x$arg == x ]]
then
    export HADOOP_CLASSPATH=target/classes
    echo "+++++++++++++++++++++++++Begin"
    # hadoop URLCat hdfs://localhost/user/$USER/$0
    hadoop FileSystemCat hdfs://localhost/user/$USER/$0
    echo "+++++++++++++++++++++++++End"
fi

if [[ x$arg == x0 ]]
then
    stop-dfs.sh
    ../../../post-stop.sh
fi
