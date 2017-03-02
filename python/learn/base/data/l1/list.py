#!/usr/bin/python2.7
#coding:utf-8

print dir(list)

l = [x for x in range(10)]

print l.__class__

l.append('d')
l.insert(0, 0)
l.insert(3, 'a')
print l
print l.count('a')
l.pop() # 最后一个
print l
l.pop(0)
print l
l.remove('a')
print l
l.reverse()
print l
l.sort(reverse=True)
for x in l:
    print x,
