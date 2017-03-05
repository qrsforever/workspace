#!/usr/bin/python3
#coding:utf-8

import numpy as np

print(np.__version__)
# print (dir(np))

a = np.array([1,2,3,4])
print(a)

b = np.array((5,6,7,8))
print(b)

# 使用list或者tuple结果是一样的
a[0] = 100
print(a)
b[0] = 500
print(b)

c = np.array([[1,2,3], [2,3,4], [3,4,5], [4,5,6]])
print(c)
c[1][0] = 200
print(c)

print(c.shape)
c.shape = 3,4
print(c)

# 一维,多维转换
a.shape = 2, 2
print(a)
c.shape = 1, -1 # -1 表示自动计算轴长
print(c)

d = b.reshape(2,2) # b 不改变
print(b)
print(d)
