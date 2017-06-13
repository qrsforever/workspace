#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

#  [[0 1 2 3 4]
#   [5 6 7 8 9]]
a = np.arange(10).reshape(2, 5)
print(a)

b = np.arange(100, 50, -2)
print(b)

#  c的形状和a相同
c = b[a]
print(c)

d = b.reshape(-1, 5)
print(d)

f = np.array([True, False, True, False, True])
print(f)

#  f作为第一维度选在数组
g = d[f, 0]
print(g)

h = d[0]
print(h)

i = d[0][0]
print(i)

# [ True False False  True]
j = np.array(['aa', 'bb', 'cc', 'aa'])
k = (j == 'aa')
print(k)

