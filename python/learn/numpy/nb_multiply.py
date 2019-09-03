#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np


###### list

##
a = [1, 2, 3]
b = [4, 5, 6]

a, b
# Out[2]: ([1, 2, 3], [4, 5, 6])

## 
a * b
# TypeError: can't multiply sequence by non-int of type 'list'

##
np.multiply(a, b)
# Out[4]: array([ 4, 10, 18])

##
np.dot(a, b)
# Out[5]: 32

###### ndarray

##
c = np.asarray(a)
d = np.asarray(b)

c, d
# Out[6]: (array([1, 2, 3]), array([4, 5, 6]))

##
c * d
# Out[7]: array([ 4, 10, 18])

##
np.multiply(c, d)
# Out[8]: array([ 4, 10, 18])

##
np.dot(c, d)
# Out[9]: 32


###### constant

##
a * 3
# Out[10]: [1, 2, 3, 1, 2, 3, 1, 2, 3]

##
c * 3
# Out[11]: array([3, 6, 9])

##
np.multiply(a, 3)
# Out[6]: array([3, 6, 9])


###### mixture

##
np.dot(c, a) # = np.dot(a, c)
# Out[14]: 14 = 1*1 + 2*2 + 3*3

##
np.multiply(c, a)
# Out[16]: array([1, 4, 9])


###### T

## 1-D
c, c.T, c.reshape((len(c), -1))
# Out[16]: (array([1, 2, 3]), array([1, 2, 3]), array([[1],
#         [2],
#         [3]]))

## 2-D
e = np.array([[1,2,3], [4,5,6]])
e, e.T, e.reshape(len(e[0]), len(e))
# Out[18]: (array([[1, 2, 3],
#         [4, 5, 6]]), array([[1, 4],
#         [2, 5],
#         [3, 6]]), array([[1, 2],
#         [3, 4],
#         [5, 6]]))

## Mul
t = 3
x = np.array([t])
y = np.array([[t]])
f = c.reshape((len(c)), -1)
x, y, f
# Out[23]: (array([3]), array([[3]]), array([[1],
#         [2],
#         [3]]))

##
f * t, f * x, f * y
# Out[25]: (array([[3],
#         [6],
#         [9]]), array([[3],
#         [6],
#         [9]]), array([[3],
#         [6],
#         [9]]))
