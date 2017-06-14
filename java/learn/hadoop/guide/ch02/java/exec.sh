#!/bin/bash

# 生成pom.xml
# mvn archetype:generate
# 编译
# mvn package

export HADOOP_CLASSPATH=target/learn-hadoop-1.0-SNAPSHOT.jar
# export HADOOP_CLASSPATH=target/classes

if [[ -d output ]]
then
    rm -rf output
fi

data_file=../bj_data.txt

cd ../
./gen_data.sh
cd -

hadoop MaxTemperature $data_file output

if [[ -f output/part-r-00000 ]]
then
    cat output/part-r-00000
fi
