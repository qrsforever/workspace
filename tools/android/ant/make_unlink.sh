#!/bin/bash
# 更新android sdk, 导致ant编译不了的临时方案

current_dir=`pwd`
tools_dir='/opt/android/tools'

make_link()
{
    if [ -L $tools_dir/$1/$2 ]
    then
        rm -f $tools_dir/$1/$2
    fi
}

make_link ant build.xml
make_link ant uibuild.xml
make_link lib ant-tasks.jar
make_link lib common.jar
make_link lib emma.jar 
make_link lib emma_ant.jar
make_link lib guava-17.0.jar
make_link lib manifest-merger.jar
make_link lib sdklib.jar
make_link lib gson-2.2.4.jar

