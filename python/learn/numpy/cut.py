#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import numpy as np

sizes = np.array([2, 3, 1])

sizes[1:]  # array([3, 1])
sizes[:-1] # array([2, 3])


###
b = [np.random.randn(y, 1) for y in sizes[1:]]
b

###
c = [np.random.randn(3, 1), np.random.randn(1, 1)]
c

###
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
data

### 
np.random.shuffle(data)
data

### that's not your desire
random.shuffle(data)
data


### that's ok for 1-d
a = [10,20,30,40,50,60]
random.shuffle(a)
a

### that's ok for 2-d
d = [(1,2,3), (4,5,6), (7,8,9)]
random.shuffle(d)
d

###
biases = [np.random.randn(y, 1) for y in sizes[1:]]
weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
print(biases, np.shape(biases))
print(weights, np.shape(weights))

for b, w in zip(biases, weights):
    print('\n')
    print(b)
    print(w)
