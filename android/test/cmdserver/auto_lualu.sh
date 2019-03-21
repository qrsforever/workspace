#!/system/bin/sh

setenforce 0

log_file=/data/lualu.txt
pid_file=/data/lualu.pid

busybox=`which busybox`

sid=`getprop ro.boot.serialno`
# redmi: c060751
# xiaomi: 56ed266
# leshi: b37da191
# shixuan: LE67A06120111457
# google: 06816cef0b3535c2

if [[ $sid == "b37da191" ]]
then
    # first parameter is ui
    shift
fi

if [[ ! -f $pid_file ]]
then
    touch $pid_file
fi

last_pid=`cat $pid_file`

echo "shell pid $$, caller args: $*, last pid: $last_pid" > $log_file

if [[ x$last_pid != x ]]
then
    kill -9 $last_pid
fi

if [[ x$1 == xkill ]]
then
    echo "kill last pid: $last_pid" >> $log_file
    pid1=`ps | grep "com.android.test.qutoutiao"`
    pid2=`ps | grep "com.android.test.cashtoutiao"`
    pid3=`ps | grep "com.android.test.toutiaoduoduo"`
    if [[ x$pid1 != x ]]
    then
        pid=`echo "$pid1" | $busybox cut -d\  -f4`
        if [[ x$pid != x ]]
        then
            kill -9 $pid
            echo "kill com.android.test: $pid" >> $log_file
        fi
    fi

    if [[ x$pid2 != x ]]
    then
        pid=`echo "$pid2" | $busybox cut -d\  -f4`
        if [[ x$pid != x ]]
        then
            kill -9 $pid
            echo "kill com.android.test: $pid" >> $log_file
        fi
    fi

    if [[ x$pid3 != x ]]
    then
        pid=`echo "$pid3" | $busybox cut -d\  -f4`
        if [[ x$pid != x ]]
        then
            kill -9 $pid
            echo "kill com.android.test: $pid" >> $log_file
        fi
    fi
    exit 0	
fi

echo $$ > $pid_file 

max=23
min=7

hui=1
qu=1
duo=1
sltm=10

if [[ x$1 == x0 ]]
then
    hui=0
fi

if [[ x$2 == x0 ]]
then
    qu=0
fi

if [[ x$3 == x0 ]]
then
    duo=0
fi

sleep 3

_run_am_instrument() {
    echo "run am : $1" >> $log_file
    am instrument -w com.android.test.$1.test/android.support.test.runner.AndroidJUnitRunner
    sleep $sltm
}

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
        # if [ "$(dumpsys power | grep state= | grep -oE '(ON|OFF)')" == OFF ]
        # then
        #     input keyevent POWER
        # fi
        input swipe 500 1080 500 600 500
    elif [[ x$sid == x"56ed266" ]]
    then
        input swipe 500 1080 500 600 500
    elif [[ x$sid == x"b37da191" ]]
    then
        input swipe 500 2080 500 600 500
    elif [[ x$sid == x"88e0b2bb" ]]
    then
        if [ "$(dumpsys power | grep mScreenOn= | grep -oE '(true|false)')" == false ]
        then
            input keyevent POWER
        fi
        input swipe 500 1080 500 600 500
    else
        input swipe 500 1080 500 600 500
    fi

    input keyevent HOME

    (( r=$RANDOM % 3 ))

    echo "random: $r" >> $log_file
    if [[ x$r == x"0" ]]
    then
        if [[ x$hui == x"1" ]]
        then
            _run_am_instrument cashtoutiao
        fi
        if [[ x$duo == x"1" ]]
        then
            _run_am_instrument toutiaoduoduo
        fi
        if [[ x$qu == x"1" ]]
        then
            _run_am_instrument qutoutiao
        fi
    elif [[ x$r == x"1" ]]
    then
        if [[ x$qu == x"1" ]]
        then
            _run_am_instrument qutoutiao
        fi
        if [[ x$hui == x"1" ]]
        then
            _run_am_instrument cashtoutiao
        fi
        if [[ x$duo == x"1" ]]
        then
            _run_am_instrument toutiaoduoduo
        fi
    elif [[ x$r == x"2" ]]
    then
        if [[ x$duo == x"1" ]]
        then
            _run_am_instrument toutiaoduoduo
        fi
        if [[ x$hui == x"1" ]]
        then
            _run_am_instrument cashtoutiao
        fi
        if [[ x$qu == x"1" ]]
        then
            _run_am_instrument qutoutiao
        fi
    fi
done

echo "never run here" >> $log_file

# adb uninstall com.android.test.[qutoutiao|cashtoutiao|toutiaoduoduo]
# adb uninstall com.android.test.[qutoutiao|cashtoutiao|toutiaoduoduo].test
