#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

a = np.array([
    [1, 1, 1], 
    [2, 2, 2], 
    [3, 3, 3]
    ])

a1 = [
    [1, 1, 1], 
    [2, 2, 2], 
    [3, 3, 3]
    ]

b = np.array([
    [1, 0, 1], 
    [2, 0, 2], 
    [3, 0, 3]
    ])

b1 = [
    [1, 0, 1], 
    [2, 0, 2], 
    [3, 0, 3]
    ]

# 转变成矩阵
c = np.mat(a)
d = np.mat(b)
f = np.mat(a1)
g = np.mat(b1)

print("a = ", a, "\na1 = ", a1)
print("b = ", b, "\nb1 = ", b1)
print("a*2 = ", a*2, "\na1*2 = ", a1*2) # 这个结果很特别， a1*2元素多了一倍，元素值没有变化
print("a+b = ", a + b)
print("a1+b1 = ", a1 + b1) # 两个数组集合的合并
print("a*b = ", a * b) # 数组相乘， not 矩阵相乘
#  print(a1 * b1) # 错误

print("c = ", c)
print("d = ", d)
print("c*d = ", c * d) # 矩阵相乘
print("f = ", f)
print("g = ", g)
print("f*g = ", f * g)
