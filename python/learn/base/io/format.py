#!/usr/bin/python2.7
#coding:utf-8

import datetime

today = datetime.datetime.now()
print str(today)
print repr(today)

# print type(eval(str(today))) # 失败, 这就是str和repr的区别之一
print type(eval(repr(today)))

x = 1.11
y = 2.22

sx = 'x is ' + str(x) 
sy = 'y is ' + repr(y) 
print sx
print sy

s = "Hello\n"
print str(s)
print repr(s)

for x in range(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4)


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}' . format(x, x*x, x*x*x))

print('[%8s] [%-6.2s]' % ('aaaa', 'bbbbb'))
