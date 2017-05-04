#!/bin/bash

# ================ Normal ================
for v in 0 1 2 3
do
    g_map[$v]="${v}_val"
done

for v in ${g_map[@]}
do
    echo $v
done

# ================ Abnormal ===============

cnt=0
echo -e "0\n1\n2\n3\n" | while read v
do
    echo "==== $v"
    g_map2[$cnt]=$v
    var="Hello"
    cnt=`expr $cnt + 1`
done

echo "---> $var"
for v in ${g_map2[@]}
do
    # 没有走到这里, 猜测是管道(|)的问题 
    echo $v
done
