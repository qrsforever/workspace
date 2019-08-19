#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

# 3x2
a = [[1, 2],
     [2, 3],
     [3, 4]]

b = [[9, 8],
     [8, 7],
     [7, 6]]

print('------------------------------')

# two list meld
print(a + b)
# output: [[1, 2], [2, 3], [3, 4], [9, 8], [8, 7], [7, 6]]

c = [x+y for x, y in zip(a, b)]
print(c)
# output: [[1, 2, 9, 8], [2, 3, 8, 7], [3, 4, 7, 6]]

print('------------------------------')

aa = np.array(a)
bb = np.array(b)

print(aa)
print(bb)

print('------------------------------')

print(type(aa))
# element of two ndarray do plus operate
cc = aa + bb

print(cc)
# output: [[10 10]
#          [10 10]
#          [10 10]]
