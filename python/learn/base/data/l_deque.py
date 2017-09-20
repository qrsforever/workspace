#!/usr/bin/python3
#coding:utf-8

from collections import deque 

a = deque([1,2,3], maxlen=5)
a.append(4)
a.append(5)
a.append(6)
print(str(a))
a.appendleft(1)
print(str(a))

print(a.pop())
print(a.popleft())
print(a)
