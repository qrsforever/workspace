if [[ x$HADOOP_HOME == x ]]
then
    echo "not set HADOOP_HOME envirnment"
    exit 0
fi

if [[ -d input ]]
then
    rm -rf input
fi

if [[ -d output ]]
then
    rm -rf output
fi

mkdir input

cp $HADOOP_HOME/etc/hadoop/*.xml input
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-$HADOOP_VERSION.jar grep input output 'dfs[a-z.]+'
