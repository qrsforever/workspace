#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np


a = np.array([[1,2,3], [4,5,6]])
# b = np.array([[1], [2], [3]])
# b = np.array([1, 2, 3])
b = [1,2,3]
c = np.dot(a, b)
print(a)
print("-------------")
print(b)
print("-------------")
print(c)

print("-----")

x = [1,2,3,4]
print(np.transpose(x))

print(np.reshape(x, (len(x), 1)))


print('----------------')
print(np.reshape(x, (4,1)))
print('---------------')
print(np.reshape(x, (1,4)))
