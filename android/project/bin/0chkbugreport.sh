#!/bin/bash

if (( $# < 1 ))
then
    echo "Use: 0chkbugreport.sh bugreport.txt"
    exit
fi

current_dir=`pwd`
cmd_dir=`which $0`
cmd_dir=`dirname $cmd_dir`

TOOLS_HOME="$cmd_dir/../tools"

java -jar $TOOLS_HOME/chkbugreport.jar $1
