#!/bin/bash
# adb shell 'echo 120 > /data/bootchart-start'
# cd /data/bootchart
# busybox tar -czf bootchart.tgz *

if (( $# < 1 ))
then
    echo "Use: 0bootchart.sh a.tgz"
    exit
fi

current_dir=`pwd`
cmd_dir=`which $0`
cmd_dir=`dirname $cmd_dir`

TOOLS_HOME="$cmd_dir/../tools"

java -jar $TOOLS_HOME/bootchart.jar $1
