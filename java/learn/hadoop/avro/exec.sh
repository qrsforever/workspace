#!/bin/bash
# source exec.sh

proname=`basename $0`
AVRO_VER=1.8.2

__exec__() 
{
    export HADOOP_USER_CLASSPATH_FIRST=true
    export HADOOP_CLASSPATH=$AVRO_HOME/avro-${AVRO_VER}.jar:$AVRO_HOME/avro-mapred-${AVRO_VER}-hadoop2.jar

    if [[ -d output ]]
    then
        rm -rf output
    fi

    hadoop jar target/learn-avro-1.0.0.jar com.java.learn.AvroGenericMaxTemperature sample.txt output
}

# cd $HADOOP_HOME
# if [[ -f etc.tar.gz ]]
# then
#     rm -rf etc
#     tar zxf etc.tar.gz 
# fi
# cd -

if [ x$proname == x"exec.sh" ]
then
    mvn package
else
    echo "pom.xml(mvn package)已经集成运行hadoop程序"
    __exec__
fi

if [ -f output/part-r-00000.avro ]
then
    java -jar $AVRO_HOME/avro-tools-${AVRO_VER}.jar tojson  output/part-r-00000.avro
fi
