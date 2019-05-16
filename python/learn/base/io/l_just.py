#!/usr/bin/python3
# -*- coding: utf-8 -*-

a = "aaa bbb ccc"

# 第二个参数是填充字符, 默认是空格
print(a.ljust(20, '+'))
print(a.rjust(20, '+'))
print(a.center(20, '+'))

print(format(a, '>20'))
print(format(a, '<20'))
print(format(a, '^20'))
print(format(a, '+>20s'))
print(format(a, '+<20s'))
print(format(a, '+^20s'))

b = 1111
print(format(b, '0>10d'))
c = 22.22
print(format(c, '0<10.4f')) # 10为宽度， 4为精确度
print(format(c, '0>10.4f'))

print('{:!>6s} {:0<8.5f} {:0^6d}'.format('aaa', 31.4, 11))
