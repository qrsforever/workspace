#!/usr/bin/python2.7
#coding:utf-8

print dir(set)

s = {'x', 'y', 'z'}
print len(s)
# print s.count('x') # 错误， Set里面的元素没有重复的, 方法没有意义

a = set('aabbccdef')
print a
b = set('abcdeffgg')
print b

print a - b  # 在a中不在b中
print a | b
print a & b
print a ^ b  # 不同时在a，b中

print { x for x in 'abcdefg' if x not in 'cdef' }
