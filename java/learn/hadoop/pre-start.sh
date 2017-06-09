#!/bin/bash

if [[ x$HADOOP_HOME == x ]]
then
    echo "not set HADOOP_HOME envirnment"
    exit 0
fi

root=$HADOOP_HOME 
curdir=`pwd`
files=`ls etc`

# 软链接配置
for file in $files
do
    echo "$file"
    if [[ -f $root/etc/hadoop/$file ]]
    then
        mv $root/etc/hadoop/$file $root/etc/hadoop/${file}.bak
    fi
    if [[ -L $root/etc/hadoop/$file ]]
    then
        rm -f $root/etc/hadoop/$file
    fi
    ln -s $curdir/etc/$file $root/etc/hadoop/$file
done

# 软链接日志目录
if [[ -L $root/logs ]]
then
    rm -f $root/logs
fi

if [[ -d $root/logs ]]
then
    rm -rf $root/logs
fi

if [[ ! -d logs ]]
then
    mkdir logs
fi

ln -s $curdir/logs $root/logs
