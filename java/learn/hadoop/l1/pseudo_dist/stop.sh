#!/bin/bash

if [[ x$HADOOP_HOME == x ]]
then
    echo "not set HADOOP_HOME envirnment"
    exit 0
fi

$HADOOP_HOME/sbin/stop-dfs.sh 

# 最后执行 ../../post-stop.sh
