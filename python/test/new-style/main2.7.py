#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

class A:
    pass

class B:
    pass


# 新式类 统一了 type(x) 和 x.__class__, python3所有类默认继承object
class C(object):
    pass

a = A()
b = B()
c = C()

print(type(A))
print(type(B))
print(type(C))

print("-------------- ")

print(type(a))
print(type(b))
print(type(c))

print("-------------- ")

print(a.__class__)
print(b.__class__)
print(c.__class__)

# output:
#  <type 'classobj'>
#  <type 'classobj'>
#  <type 'type'>
#  --------------
#  <type 'instance'>
#  <type 'instance'>
#  <class '__main__.C'>
#  --------------
#  __main__.A
#  __main__.B
#  <class '__main__.C'>

