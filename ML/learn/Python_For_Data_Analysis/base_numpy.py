#!/usr/bin/python3
# -*- coding: utf-8 -*-

## jupyter console

import numpy as np

##
data = [[1,2,3,4],[5,6,7,8]]
arr1 = np.array(data)
type(arr1)
arr1.ndim
arr1.shape
np.zeros((3,2))
np.empty((3,2,2))
np.arange(10)

##
arr1 * arr1
arr1 * 0
arr1 + 1

##
arr2 = np.arange(10)
arr2[2]
arr3 = np.array([[1,2,3],[4,5,6]])
arr3[0]
arr3[0][1]

##
arr2[:3]
arr2[:-3]
arr3[1:, :2]

##
arr3 < 5
arr3[arr3 < 5]

##
arr4 = np.empty((8,4))
for i in range(8):
    arr4[i] = i
arr4

##
arr5 = np.arange(32).reshape((8,4))
arr5

##
arr5.shape
arr6 = arr5.T
arr6.shape

##
arr7 = np.random.randn(6, 3)
arr7
np.dot(arr7.T, arr7)

##
arr8 = np.arange(16).reshape((2,2,4))
arr8
arr8.transpose((2, 1, 0))

##
arr9 = np.arange(1, 17)
arr9
np.sqrt(arr9)
np.exp(arr9)

## 用数组表达式代替循环: 矢量化
arr10 = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(arr10, arr10)
ys
z = np.sqrt(xs ** 2 + ys ** 2)
z

## broadcast
arr11 = np.arange(12).reshape((3,4))
arr11
arr11[0]
arr11 - arr11[0]
