#!/bin/bash

_fun()
{
    echo "1"
    echo "2"
    return "3"
    # return 200
}

# 返回1, 2 是输出
ret1=`_fun`

echo "#############a"

echo $ret1

echo "#############b"

_fun

# 返回的是3, 是结果, 只能是数值型
echo "return: $?"

echo "#############c"
