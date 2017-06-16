#!/bin/bash

if [[ x$HADOOP_HOME == x ]]
then
    echo "not set HADOOP_HOME envirnment"
    exit 0
fi

root=$HADOOP_HOME 
curdir=`pwd`
files=`ls $root/etc/hadoop`

# 恢复配置
for file in $files
do
    if [[ -L $root/etc/hadoop/$file ]]
    then
        rm -f $root/etc/hadoop/$file
        if [[ -f $root/etc/hadoop/${file}.bak ]]
        then
            echo $file
            mv $root/etc/hadoop/${file}.bak $root/etc/hadoop/$file
        fi
    fi
done

if [[ -L $root/logs ]]
then
    rm -f $root/logs
fi

if [[ -d logs ]]
then
    rm -rf logs
fi
