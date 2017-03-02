#!/usr/bin/python2.7
#coding:utf-8

def getFunc(n):
    return lambda x, y: x**n + y**n

f = getFunc(2)
print '1**2 + 2**2 = ',  f(1,2)
print '2**2 + 3**2 = ',  f(2,3)

f = getFunc(3)
print '1**3 + 2**3 = ',  f(1,2)
print '2**3 + 3**3 = ',  f(2,3)
