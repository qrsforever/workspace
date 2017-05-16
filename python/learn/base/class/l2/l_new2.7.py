#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

class A:
    def __init__(self):
        print("A.__init__")
        #  super(A, self).__init__() # Wrong


# False: 经典类(非新式类)
print(issubclass(A().__class__, object))

class B(object):
    def __init__(self):
        print("B.__init__")
        super(B, self).__init__() # OK, 非pytho3版本, super需要正确的参数

# True: 新式类 (可以使用super)
print(issubclass(B().__class__, object))
