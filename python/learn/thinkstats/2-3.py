#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Pmf
import operator

#  编写一个 Mode 函数(众数),以 Hist 对象为参数,返回最频繁值
def Mode(hist):
    max = 0
    key = 0
    for k, v in hist.Items():
        print(k, v)
        if v > max:
            max = v
            key = k
    return key

# 编写一个 AllModes 函数,参数还是 Hist 对象,但返回的是按频数降序排列的值—频数对
def AllModes(hist):
    return sorted(hist.Items(), key = operator.itemgetter(1), reverse = True)

if __name__ == "__main__":
    hist = Pmf.MakeHistFromList([5, 2, 5, 3, 2, 5, 7, 2], name='test')
    print("Mode(hist) = ", Mode(hist))
    print("AllModes(hist) = ", AllModes(hist))
