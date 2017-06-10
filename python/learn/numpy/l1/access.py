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
print(a[5:1:-2]) # 步长为负数, 起始下标大于结束下标

# 通过切片创建共享视图
b = a[1:5]
b[0] = 100
b[3] = 400
print('{0} {1}'.format(a, b)) # 也会发生改变

# 整数序列(不改变原数组) 
c = np.arange(12, 0, -2)
c1 = c[[0,2,4]]
c1[0] = c1[0] * 10
print(c, c1)

# 整数数组(不改变原数组)
d = c[np.array([0, 2, 4])]
d[0] = 100
print(c, np.array([0, 2, 4]), d)
d1 = c[np.array([[1, 3, 5], [0, 2, 4]])]
print(d1)
