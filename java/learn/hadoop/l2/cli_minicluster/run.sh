#!/bin/bash 

if [[ x$HADOOP_HOME == x ]]
then
    echo "not set HADOOP_HOME envirnment"
    exit 0
fi

# resource manager port
RM_PORT=7701
HS_PORT=7702

# error
HADOOP_CLASSPATH=$HADOOP_HOME/share/hadoop/yarn/test/hadoop-yarn-server-tests-2.8.0-tests.jar $HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-2.8.0-tests.jar minicluster -rmport $RM_PORT -jhsport $JHS_PORT

