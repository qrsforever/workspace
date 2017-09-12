#!/usr/bin/python3
# -*- coding: utf-8 -*-

data = [1,2,3,4]

def foo():
    yield 1
    yield 2
    yield 3
    yield 4


for i in data:
    print(i)

print("-------------- ")

for i in iter(data):
    print(i)

print("-------------- ")

for i in foo():
    print(i)

print("-------------- ")

for i in iter(foo()):
    print(i)
