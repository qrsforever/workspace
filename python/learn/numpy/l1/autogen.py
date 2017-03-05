#!/usr/bin/python3
#coding:utf-8

import numpy as np

print(np.arange(0, 100, 5, np.int32))

a = np.linspace(0, 50, 5)
b = np.linspace(0, 50, 5, endpoint=False)
print(a.dtype)
print(a)
print(b.dtype)
print(b)

c = np.logspace(0, 2, 5) # default base:10, [10^0 --> 10^2]
print(c)
d = np.logspace(0, 2, 5, base = 2, endpoint=False)
print(d)

e1 = np.zeros(10)
e2 = np.zeros((2, 3), dtype=np.float64)
print(e1)
print(e2)

f1 = np.ones(10, dtype=complex)
print(f1.dtype)
print(f1)
f2 = np.ones([3, 2])
print(f2.dtype)
print(f2)

s = "abcdefgh"
g1 = np.fromstring(s, np.int8)
print(g1)
g2 = np.fromstring(s, dtype=np.int16) # s字符数必须是偶数个
print(g2)

# shape为一维
def func1(i):
    return i % 5 + 1;

h1 = np.fromfunction(function=func1, shape=(10,))
print(h1)

# shape为二维
def func2(i, j):
    return i % 5 + j % 3;

h2 = np.fromfunction(func2, shape=(3, 5))
print(h2)

