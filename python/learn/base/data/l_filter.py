#!/usr/bin/python3
# -*- coding: utf-8 -*-

a = [1, 3, -1, -7, 2, 4, -6]
b = [n if n > 0 else 0 for n in a]
print(b)
c = [n for n in a if n > 0]
print(c)

"""
c = (a > b) ? a : b
等价于
c = a if a > b else b
"""
