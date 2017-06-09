#!/bin/bash

if [[ x$HADOOP_HOME == x ]]
then
    echo "not set HADOOP_HOME envirnment"
    exit 0
fi

$HADOOP_HOME/sbin/stop-yarn.sh 
$HADOOP_HOME/sbin/stop-dfs.sh 
