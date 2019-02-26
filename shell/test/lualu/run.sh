#!/bin/bash

aa=$1

max=22
min=7
while ((1))
do
    hour=`date +"%-H"`
    day=`date +"%-d"`
    echo "now hour: $hour"
    if (( $day == "04" || $day == "05" || $day == "06" || $day == "07" ))
    then
        max=20
        min=10
    fi
        
    if (( $hour > $max || $hour < $min ))
    then
        echo "sleep..."
        sleep 900
    else
        if [[ x$aa == x"xiaomi" ]]
        then
            adb -s 56ed266a shell input keyevent 3
            sleep 1
            adb -s 56ed266a shell input swipe 500 1080 500 600 500
            sleep 1
            ./lualu.sh "56ed266a"
        elif [[ x$aa == x"redmi" ]]
        then
            ./lualu.sh "c060751"
        elif [[ x$aa == x"leshi" ]]
        then
            ./lualu.sh "b37da191"
        elif [[ x$aa == x"shixuan" ]]
        then
            ./lualu.sh "LE67A06120111457"
        else
            echo "not support"
            exit 0
        fi
    fi
done
