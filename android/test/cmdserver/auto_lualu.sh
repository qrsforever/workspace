#!/system/bin/sh

setenforce 0

log_file=/data/lualu.txt
pid_file=/data/lualu.pid

mv $log_file ${log_file}_bak
echo "shell pid $$, caller args: $*" > $log_file

cut="cut"
sid=`getprop ro.boot.serialno`
if [[ $sid == "c060751" ]]
then
    __myecho "red mi"
    cut="toybox cut"
elif [[ $sid == "56ed266" ]]
then
    __myecho "xiao mi"
elif [[ $sid == "b37da191" ]]
then
    __myecho "leshi"
    # first parameter is ui
    shift
elif [[ $sid == "88e0b2bb" ]]
then
    __myecho "oppo"
    cut="busybox cut"
fi

__myecho() {
    dt=`date`
    echo "$dt:$*" >> $log_file
}

_kill_android_test() {
    pidstr=`ps | grep "com.android.test.$1"`
    if [[ x$pidstr != x ]]
    then
        __myecho "test: $pidstr"
        pid=`echo $pidstr | $cut -d\  -f2`
        __myecho "parse pid = $pid"
        if [[ x$pid != x ]]
        then
            kill -9 $pid
            __myecho "kill com.android.test.$1[$pid]"
        else
            __myecho "no com.android.test.$1 pid"
        fi
    else
        __myecho "no com.android.test.$1 process"
    fi
}

_kill_android_test qutoutiao
_kill_android_test cashtoutiao
_kill_android_test toutiaoduoduo

__read_pid() {
    if [[ ! -f $pid_file ]]
    then
        pid=
    else
        pid=`cat $pid_file`
    fi
    echo $pid
}

last_pid=$(__read_pid)

if [[ x$last_pid != x ]]
then
    kill -9 $last_pid
    __myecho "kill last pid: $last_pid"
    rm $pid_file
fi

if [[ x$1 == xkill ]]
then
    exit 0	
fi

curr_pid=$$
echo $curr_pid > $pid_file 

_run_am_instrument() {
    __myecho "run am : $1"
    am instrument -w com.android.test.$1.test/android.support.test.runner.AndroidJUnitRunner
    if [[ x$curr_pid != x$(__read_pid) ]]
    then
        __myecho "curr_pid:$curr_pid vs last_pid: $last_pid"
        exit -1
    fi
    sleep $sltm
}

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

sleep 2

while ((1))
do
    hour=`date +"%-H"`
    day=`date +"%-d"`
    __myecho "now hour: $hour"
    if (( $hour > $max || $hour < $min ))
    then
        __myecho "sleep..."
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
    elif [[ x$sid == x"LE67A06120111457" ]]
    then
        input swipe 500 1080 500 200 500
    else
        input swipe 500 1080 500 600 500
    fi

    input keyevent HOME

    (( r=$RANDOM % 3 ))

    __myecho "random: $r"
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

__myecho "never run here"

# adb uninstall com.android.test.[qutoutiao|cashtoutiao|toutiaoduoduo]
# adb uninstall com.android.test.[qutoutiao|cashtoutiao|toutiaoduoduo].test
