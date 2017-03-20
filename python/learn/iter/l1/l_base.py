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
