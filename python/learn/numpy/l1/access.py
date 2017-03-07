#!/usr/bin/python3
#coding:utf-8

import numpy as np

# 切片访问
a = np.arange(0, 10, 1)
print(a)
print(a[1])
print(a[1:3])
print(a[:3])
print(a[::])
print(a[1:-1]) # 负数表示倒数第x个
print(a[1:5:2])
print(a[5:1:-2]) # 步长为负数, 起始下标大于结束下表

# 通过切片创建共享视图
b = a[1:5]
b[0] = 100
print(b)
print(a) # 也会发生改变

# 整数序列(不改变原数组) 
# c = np.array(a[
