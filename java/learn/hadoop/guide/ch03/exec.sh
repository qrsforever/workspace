#!/bin/bash

# 生成pom.xml
# mvn archetype:generate
# 编译
# mvn compile or package

# 从Hadoop URL中读取数据

arg=$1

datafile=data.txt

if [[ x$arg == x1 ]]
then
    ../../pre-start.sh
    hdfs namenode -format -nonInteractive
    start-dfs.sh 
    # 必须先创建一个用户， 相对路径就是/user/$USER
    hadoop fs -mkdir -p /user/$USER

    rm -f $datafile
    for i in `seq 10`
    do
        echo -n "123456789$i" >> $datafile
    done

    hadoop fs -copyFromLocal -f $datafile $datafile
fi

if [[ x$arg == x ]]
then
    export HADOOP_CLASSPATH=target/classes
    # hadoop URLCat hdfs://localhost/user/$USER/$0
    # hadoop FileSystemCat hdfs://localhost/user/$USER/$datafile
    hadoop FileCopyWithProgress $datafile hdfs://localhost/user/$USER/${datafile}.bak
fi

if [[ x$arg == x0 ]]
then
    rm -f $datafile
    stop-dfs.sh
    ../../post-stop.sh
fi
