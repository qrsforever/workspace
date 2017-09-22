if [[ x$HADOOP_HOME == x ]]
then
    echo "not set HADOOP_HOME envirnment"
    exit 0
fi

yarnservr=$HADOOP_HOME/share/hadoop/yarn/test/hadoop-yarn-server-tests-$HADOOP_VERSION-tests.jar 
jobclient=$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-$HADOOP_VERSION-tests.jar

HADOOP_CLASSPATH=$yarnservr $HADOOP_HOME/bin/hadoop jar $jobclient minicluster
