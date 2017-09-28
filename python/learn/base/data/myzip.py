#!/usr/bin/python3
# -*- coding: utf-8 -*-

# e1:

dicts = { 'a':1, 'b':2, 'c':3 }
# 返回: 'a':1 ===> (a, 1)
print("type(dicts.items()) = ", dicts.items())
print("items", dicts.items())
# Tuple tar, 将所有元组,按列打包
xs, ys = zip(*dicts.items())
print("xs:", xs) # 元组第1列
print("ys:", ys) # 元组第2列

# e2:

data = ((1, 2, 3), ('a', 'b', 'c'), ('!', '@', '#'))
xs, ys, zs = zip(*data)
print("xs:", xs) # 元组第1列 (1, 'a', '!')
print("ys:", ys) # 元组第2列
print("zs:", zs) # 元组第3列
