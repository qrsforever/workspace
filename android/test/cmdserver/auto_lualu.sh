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

kill -9 $last_pid

if [[ x$1 == xkill ]]
then
    echo "kill $last_pid" > $log_file
    pid1=`ps | grep "com.android.test.qutoutiao"`
    pid2=`ps | grep "com.android.test.cashtoutiao"`
    pid3=`ps | grep "com.android.test.toutiaoduoduo"`
    if [[ x$pid1 != x ]]
    then
        pid=`echo "$pid1" | busybox cut -d\  -f4`
        kill -9 $pid
        echo "kill com.android.test: $pid" >> $log_file
    fi

    if [[ x$pid2 != x ]]
    then
        pid=`echo "$pid2" | busybox cut -d\  -f4`
        kill -9 $pid
        echo "kill com.android.test: $pid" >> $log_file
    fi

    if [[ x$pid3 != x ]]
    then
        pid=`echo "$pid3" | busybox cut -d\  -f4`
        kill -9 $pid
        echo "kill com.android.test: $pid" >> $log_file
    fi
    exit 0	
fi

echo "shell pid $$, caller pid: $1, last pid: $last_pid" > $log_file

echo $$ > $pid_file 

max=23
min=7

hui=1
qu=1
duo=1
sltm=10

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

    input keyevent WAKEUP

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

    (( r=$RANDOM % 4 ))

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

# adb uninstall com.android.test.[qutoutiao|cashtoutiao|toutiaoduoduo]
# adb uninstall com.android.test.[qutoutiao|cashtoutiao|toutiaoduoduo].test
