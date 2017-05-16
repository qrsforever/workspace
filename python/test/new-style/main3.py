#!/usr/bin/python3
# -*- coding: utf-8 -*-

class A:
    pass

class B:
    pass

a = A()
b = B()

print(type(A))
print(type(B))

print("-------------- ")

print(type(a))
print(type(b))

print("-------------- ")

print(a.__class__)
print(b.__class__)


#  output:
#  <class 'type'>
#  <class 'type'>
#  --------------
#  <class '__main__.A'>
#  <class '__main__.B'>
#  --------------
#  <class '__main__.A'>
#  <class '__main__.B'>
