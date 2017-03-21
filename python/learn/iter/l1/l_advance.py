#!/usr/bin/python3
# -*- coding: utf-8 -*-

from itertools import dropwhile
from itertools import chain

class Node():
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


    def depth_show(self):
        yield self
        for c in self:
            yield from c.depth_show() ###

root = Node(0)
c1 = Node(10)
c2 = Node(20)
c3 = Node(30)
c11 = Node(11)
c12 = Node(12)
c31 = Node(31)
root.add_child(c1)
root.add_child(c2)
root.add_child(c3)
c1.add_child(c11)
c1.add_child(c12)
c3.add_child(c31)

for node in root.depth_show():
    print(node)


class CountDown():
    def __init__(self, value):
        self._value = value

    def __iter__(self):
        n = self._value 
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 0
        while n < self._value:
            yield n
            n += 1

print("-------------- CountDown")

for c in CountDown(10):
    print(c, end=' ')
print("")

print("-------------- Reversed CountDown")

for c in reversed(CountDown(10)):
    print(c, end=' ')
print("")

print("-------------- itertool.dropwhile")

with open('./test.txt') as f:
    for line in f:
        print(line, end='')
    
print("-------------- itertool.dropwhile")

with open('./test.txt') as f:
    for line in dropwhile(lambda x : x.startswith('#'), f):
        print(line, end='') # 最后的#行没有去掉

print("-------------- itertools.chain")

s1 = set()
s1.add(10)
s1.add(11)
s1.add(12)
s2 = {21, 22, 23}
s3 = {3.0, 3.1, 3.2, 22}
# 低效， 去掉了重复的22
for x in s1 | s2 | s3:
    print(x, end=' ')
print("")
# 高效， 22重复
for x in chain(s1, s2, s3):
    print(x, end=' ')
