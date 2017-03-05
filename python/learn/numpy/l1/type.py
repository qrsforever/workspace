#!/usr/bin/python3
#coding:utf-8

import numpy as np

a = np.array([x*2 for x in range(6)], dtype=float)
print(a)

b = np.array([y*3 for y in range(6)], dtype=np.float64)
print(b)

print([key for key, value in np.typeDict.items() if value is np.float64])
print(set(np.typeDict.values()))

c = a.astype(np.int32)
print(c)

n1 = 3.14
n2 = np.float64(n1)
