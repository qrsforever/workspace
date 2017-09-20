#!/usr/bin/python2.7
#coding:utf-8

print dir(tuple)

t = (1, 3, 5, 1)
tt = t, 5, 3

print list(t)

print tt
print len(tt)
print t.count(1)
print tt.count(1)
# t[0] = 2 # 元组是不可变的
