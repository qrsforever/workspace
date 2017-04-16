#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

class LeecoPerson(object):

    """Docstring for LeecoPerson.
    看上去和attribute错不多， 访问时自动触发setter, getter, deleter方法
    只有对attribute有其他额外操作时， 比如类型检查才去考虑使用property
    """

    def __init__(self, first_name, last_name):
        """TODO: to be defined1.

        :first_name: TODO
        :last_name: TODO

        """
        self.first_name = first_name # 既然实现了该属性的getter，setter，为什么dir字典中还有'first_name'的存在
        self.last_name = last_name

    def __str__(self):
        #  return '({0.first_name!r}, {0.last_name!r})'.format(self)
        return '({0._first_name!r}, {0.last_name!r})'.format(self)
    
    @property
    def first_name(self):
        print(" first_name getter")
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        print(" first_name setter")
        if not isinstance(value, str):
            raise TypeError("Expected a string!")
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise RuntimeError("Can't delete the var")


a = LeecoPerson('Li', 'Dong')

#  a.first_name = 100 # will call first_name setter methond, 类型检测报错， 
print(a)
#  print(dir(a))
#  print (type(a.first_name))

a.first_name = 'Zhang'
print(getattr(a, 'first_name'))   # 会调用first_name.getter属性函数 
print(getattr(a, '_first_name'))  # 不会调用first_name.getter函数

#  del a.first_name

print("-------------- ")

LeecoPerson.first_name.fget(a) # 属性操作的实质
LeecoPerson.first_name.fset(a, 'Wang')

print(a)


print("-------------- ")

class LeecoCircle(object):

    """Docstring for LeecoCircle. """

    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

b = LeecoCircle(2.0)
print(b._radius)
print('{:0.2f}'.format(b.area)) # right: b.area， wrong ： b.area()
