#!/bin/bash

r=`expr $RANDOM % 4`

hui=1
qu=1
ant=0
duo=1
sltm=10

if [[ x$r == x"0" ]]
then
    if [[ x$hui == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.cashtoutiao.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
    if [[ x$qu == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.qutoutiao.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
    if [[ x$ant == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.anttoutiao.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
    if [[ x$duo == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.toutiaoduoduo.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
elif [[ x$r == x"1" ]]
then
    if [[ x$qu == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.qutoutiao.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
    if [[ x$ant == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.anttoutiao.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
    if [[ x$hui == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.cashtoutiao.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
    if [[ x$duo == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.toutiaoduoduo.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
elif [[ x$r == x"2" ]]
then
    if [[ x$ant == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.anttoutiao.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
    if [[ x$duo == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.toutiaoduoduo.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
    if [[ x$hui == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.cashtoutiao.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
    if [[ x$qu == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.qutoutiao.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
elif [[ x$r == x"3" ]]
then
    if [[ x$duo == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.toutiaoduoduo.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
    if [[ x$hui == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.cashtoutiao.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
    if [[ x$qu == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.qutoutiao.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
    if [[ x$ant == x"1" ]]
    then
        date
        adb -s $1 shell am instrument -w com.android.test.anttoutiao.test/android.support.test.runner.AndroidJUnitRunner
        sleep $sltm
    fi
else
    echo "Never"
fi
