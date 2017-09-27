#!/bin/bash

# 环境配置: ../../tutorial/pseudo_dist/setup/script.sh

# ./exec.sh  2>&1 | tee /tmp/log.txt

if [[ x$HADOOP_HOME == x ]]
then
    echo "not set HADOOP_HOME envirnment"
    exit 0
fi

# 放开所有打印 --> log4j.rootLogger=${hadoop.root.logger}
_open_debug() {
    export HADOOP_ROOT_LOGGER="ALL,console"
    # 调试库
    export HADOOP_USER_CLASSPATH_FIRST=true
    hadoop_hdfs_jar="/data/opt/hadoop/hadoop-2.7.3-src/hadoop-hdfs-project/hadoop-hdfs/target/hadoop-hdfs-2.7.3.jar"
    hadoop_comm_jar="/data/opt/hadoop/hadoop-2.7.3-src/hadoop-common-project/hadoop-common/target/hadoop-common-2.7.3.jar"
    export HADOOP_CLASSPATH="$hadoop_comm_jar:$hadoop_hdfs_jar"
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
}

_run_demo() {

    hdfs dfs -copyFromLocal pom.xml pom.xml
    hdfs dfs -ls /user/$USER

    hadoop jar target/analyze_delete-1.0-SNAPSHOT.jar com.java.learn.FileSystemDelete "hdfs://localhost:9000/user/$USER/pom.xml"
    hdfs dfs -ls /user/$USER
}

_open_debug

if [[ x$1 == x1 ]]
then
    _start_hadoop
    _run_demo 
elif [[ x$1 == x0 ]]
then
    _stop_hadoop
else
    _run_demo 
fi

