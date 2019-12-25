#!/bin/bash

# 尽量少使用$()执行子命令, 效率很低, 使用${str:}字符串处理

__func2() {
    num=0
    start=$(date)
    while read line
    do
        id=$(echo $line | cut -d, -f1)
        names=$(echo $line | cut -d, -f2)
        for name in $names
        do
            if [[ -f "${name:0:1}/${name:1:1}/${name:2:1}/${name}.jpg" ]]
            then
                echo "$id: ${name:0:1}/${name:1:1}/${name:2:1}/${name}.jpg"
            fi
        done
    done < train.csv
    end=$(data)
    echo $start "  " $end
}

__func2
