#!/bin/bash

# 环境配置: ../../tutorial/pseudo_dist/setup/script.sh

# ./exec.sh  2>&1 | tee /tmp/log.txt

if [[ x$HADOOP_HOME == x ]]
then
    echo "not set HADOOP_HOME envirnment"
    exit 0
fi

if [[ x"$1" == x"?" ]] 
then
    echo "First run for envirnment: ../../tutorial/pseudo_dist/setup/script.sh"
    echo "Start hadoop: ./exec.sh 1"
    echo "Stop hadoop: ./exec.sh 0"
    echo "Debug: ./exec.sh"
    echo "Log: ./exec.sh  2>&1 | tee /tmp/log.txt"
    exit 0
fi

# 放开所有打印 --> log4j.rootLogger=${hadoop.root.logger}
_open_debug() {
    export HADOOP_ROOT_LOGGER="ALL,console"
    # 调试库, 启动rpc相关的服务不能使用本地自己的库
    export HADOOP_USER_CLASSPATH_FIRST=true
    hadoop_hdfs_jar="/data/opt/hadoop/hadoop-2.7.3-src/hadoop-hdfs-project/hadoop-hdfs/target/hadoop-hdfs-2.7.3.jar"
    hadoop_comm_jar="/data/opt/hadoop/hadoop-2.7.3-src/hadoop-common-project/hadoop-common/target/hadoop-common-2.7.3.jar"
    # 建议直接替换原库
    if [ ! -f $HADOOP_HOME/share/hadoop/hdfs/hadoop-hdfs-2.7.3.jar.bak ]
    then
        echo "mv $HADOOP_HOME/share/hadoop/hdfs/hadoop-hdfs-2.7.3.jar $HADOOP_HOME/share/hadoop/hdfs/hadoop-hdfs-2.7.3.jar.bak"
        mv $HADOOP_HOME/share/hadoop/hdfs/hadoop-hdfs-2.7.3.jar $HADOOP_HOME/share/hadoop/hdfs/hadoop-hdfs-2.7.3.jar.bak
    fi
    cp $hadoop_hdfs_jar $HADOOP_HOME/share/hadoop/hdfs/
    if [ ! -f $HADOOP_HOME/share/hadoop/common/hadoop-common-2.7.3.jar.bak ]
    then
        echo "mv $HADOOP_HOME/share/hadoop/common/hadoop-common-2.7.3.jar $HADOOP_HOME/share/hadoop/common/hadoop-common-2.7.3.jar.bak"
        mv $HADOOP_HOME/share/hadoop/common/hadoop-common-2.7.3.jar $HADOOP_HOME/share/hadoop/common/hadoop-common-2.7.3.jar.bak
    fi
    cp $hadoop_comm_jar $HADOOP_HOME/share/hadoop/common/
    # export HADOOP_CLASSPATH="$hadoop_comm_jar:$hadoop_hdfs_jar"
}

_start_hadoop() {
    if [[ -d ~/workspace/hadoop/tmp ]]
    then
        rm ~/workspace/hadoop/tmp -rf
    fi

    if [[ -d ~/workspace/hadoop/logs ]]
    then
        rm ~/workspace/hadoop/logs -rf
    fi

    hdfs namenode -format -force -nonInteractive
    start-dfs.sh 
    hdfs dfs -mkdir -p /user/$USER
    hdfs dfs -chmod g+w /user/$USER
    hdfs dfs -ls /user/$USER
}

_stop_hadoop() {
    stop-dfs.sh

    if [ -f $HADOOP_HOME/share/hadoop/hdfs/hadoop-hdfs-2.7.3.jar.bak ]
    then
        echo  "mv $HADOOP_HOME/share/hadoop/hdfs/hadoop-hdfs-2.7.3.jar.bak $HADOOP_HOME/share/hadoop/hdfs/hadoop-hdfs-2.7.3.jar"
        mv $HADOOP_HOME/share/hadoop/hdfs/hadoop-hdfs-2.7.3.jar.bak $HADOOP_HOME/share/hadoop/hdfs/hadoop-hdfs-2.7.3.jar
    fi
    if [ -f $HADOOP_HOME/share/hadoop/common/hadoop-common-2.7.3.jar.bak ]
    then
        echo "mv $HADOOP_HOME/share/hadoop/common/hadoop-common-2.7.3.jar.bak $HADOOP_HOME/share/hadoop/common/hadoop-common-2.7.3.jar"
        mv $HADOOP_HOME/share/hadoop/common/hadoop-common-2.7.3.jar.bak $HADOOP_HOME/share/hadoop/common/hadoop-common-2.7.3.jar
    fi
}

_run_demo() {

    hdfs dfs -copyFromLocal pom.xml pom.xml
    hdfs dfs -ls /user/$USER

    # 调试库
    hadoop jar target/analyze_delete-1.0-SNAPSHOT.jar com.java.learn.FileSystemDelete "hdfs://localhost:9000/user/$USER/pom.xml"
    hdfs dfs -ls /user/$USER
}

_open_debug

if [[ x$1 == x1 ]]
then
    _start_hadoop
elif [[ x$1 == x0 ]]
then
    _stop_hadoop
else
    _run_demo 
fi

