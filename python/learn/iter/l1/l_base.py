#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

a = random.sample(range(100), 10)
print("All items: {}".format(a))

it = iter(a) # call a.__iter__()

print("Num01: {}".format(next(it))) # call it.__next__()
print("Num02: {}".format(next(it)))
print("Num03: {}".format(it.__next__()))

it = iter(a)
i = 1
while True:
    try:
        x = next(it)
        print("Num{:02d}: {}".format(i, x))
    except StopIteration:
        break
    i += 1


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
                                                                
root = Node(0)
root.add_child(Node(1))
root.add_child(Node(2))

for x in root:
    print(x)

class Node2():
    def __init__(self, value):
        self._value = value
        self._children = []
        self._idx = 0

    def __repr__(self):
        return 'Node2({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        self._idx = 0
        return self   # 返回自己， 说明自己是迭代器，须实现__next__()

    def __next__(self):
        if self._idx < len(self._children):
            idx = self._idx
            self._idx += 1
            return self._children[idx]
        raise StopIteration

root = Node2(10)
root.add_child(Node2(11))
root.add_child(Node2(22))

for x in root:
    print(x)

class Node3():
    def __init__(self, value):
        self._value = value
        self._children = []
        self._idx = 0

    def __repr__(self):
        return 'Node3({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def has_children(self):
        return len(self._children) != 0

    def __iter__(self):
        self._idx = 0
        return self   # 返回自己， 说明自己是迭代器，须实现__next__()

    def __next__(self):
        if self._idx < len(self._children):
            idx = self._idx
            self._idx += 1
            return self._children[idx]
        raise StopIteration

def recur_show(root):
    print(root)
    if root.has_children():
        for node in root:
            recur_show(node)

def recur_show2(root):
    if root.has_children():
        for node in root:
            recur_show2(node)
    print(root)

#             0
#     
#    10      20      30
# 
# 11   12          31

root = Node3(0)
c1 = Node3(10)
c2 = Node3(20)
c3 = Node3(30)
c11 = Node3(11)
c12 = Node3(12)
c31 = Node3(31)
root.add_child(c1)
root.add_child(c2)
root.add_child(c3)
c1.add_child(c11)
c1.add_child(c12)
c3.add_child(c31)

print("==================")
recur_show(root)
print("==================")
recur_show2(root)
