#!/bin/bash

log_file=/data/lualu.txt
pid_file=/data/lualu.pid

sid=`getprop ro.boot.serialno`
# redmi: c060751
# xiaomi: 56ed266
# leshi: b37da191
# shixuan: LE67A06120111457
# google: 06816cef0b3535c2

if [[ ! -f $pid_file ]]
then
    touch $pid_file
fi

last_pid=`cat $pid_file`

echo "shell pid $$, caller pid: $1, last pid: $last_pid" > $log_file

if [[ x$last_pid != x ]]
then
    kill -9 $last_pid
fi

echo $$ > $pid_file 

max=23
min=7

setenforce 0

while ((1))
do
    hour=`date +"%-H"`
    day=`date +"%-d"`
    echo "now hour: $hour" >> $log_file
        
    if (( $hour > $max || $hour < $min ))
    then
        echo "sleep..."
        sleep 900
        continue
    fi

    # 破锁屏
    if [[ x$sid == x"c060751" ]]
    then
        input swipe 500 1080 500 600 500
    elif [[ x$sid == x"56ed266" ]]
    then
        input swipe 500 1080 500 600 500
    elif [[ x$sid == x"b37da191" ]]
    then
        input swipe 500 2080 500 600 500
    else
        input swipe 500 1080 500 600 500
    fi

    input keyevent HOME

    r=`expr $RANDOM % 4`
    hui=1
    qu=1
    duo=1
    sltm=10

    echo "random: $r" >> $log_file
    if [[ x$r == x"0" ]]
    then
        if [[ x$hui == x"1" ]]
        then
            am instrument -w com.android.test.cashtoutiao.test/android.support.test.runner.AndroidJUnitRunner
            sleep $sltm
        fi
        if [[ x$qu == x"1" ]]
        then
            am instrument -w com.android.test.qutoutiao.test/android.support.test.runner.AndroidJUnitRunner
            sleep $sltm
        fi
        if [[ x$duo == x"1" ]]
        then
            am instrument -w com.android.test.toutiaoduoduo.test/android.support.test.runner.AndroidJUnitRunner
            sleep $sltm
        fi
    elif [[ x$r == x"1" ]]
    then
        if [[ x$qu == x"1" ]]
        then
            am instrument -w com.android.test.qutoutiao.test/android.support.test.runner.AndroidJUnitRunner
            sleep $sltm
        fi
        if [[ x$hui == x"1" ]]
        then
            am instrument -w com.android.test.cashtoutiao.test/android.support.test.runner.AndroidJUnitRunner
            sleep $sltm
        fi
        if [[ x$duo == x"1" ]]
        then
            am instrument -w com.android.test.toutiaoduoduo.test/android.support.test.runner.AndroidJUnitRunner
            sleep $sltm
        fi
    elif [[ x$r == x"2" ]]
    then
        if [[ x$duo == x"1" ]]
        then
            am instrument -w com.android.test.toutiaoduoduo.test/android.support.test.runner.AndroidJUnitRunner
            sleep $sltm
        fi
        if [[ x$hui == x"1" ]]
        then
            am instrument -w com.android.test.cashtoutiao.test/android.support.test.runner.AndroidJUnitRunner
            sleep $sltm
        fi
        if [[ x$qu == x"1" ]]
        then
            am instrument -w com.android.test.qutoutiao.test/android.support.test.runner.AndroidJUnitRunner
            sleep $sltm
        fi
    elif [[ x$r == x"3" ]]
    then
        if [[ x$duo == x"1" ]]
        then
            am instrument -w com.android.test.toutiaoduoduo.test/android.support.test.runner.AndroidJUnitRunner
            sleep $sltm
        fi
        if [[ x$hui == x"1" ]]
        then
            am instrument -w com.android.test.cashtoutiao.test/android.support.test.runner.AndroidJUnitRunner
            sleep $sltm
        fi
        if [[ x$qu == x"1" ]]
        then
            am instrument -w com.android.test.qutoutiao.test/android.support.test.runner.AndroidJUnitRunner
            sleep $sltm
        fi
    else
        echo "Never"
    fi
done

echo "never run here" >> $log_file
