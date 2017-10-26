#!/usr/bin/python3
# -*- coding: utf-8 -*-

str = """ACS3004 湖南新永利交通科工贸有限公司
ACS3005 三一帕尔菲格特种车装备有限公司
ACS3006 湖南新永利交通科工贸有限公司"""

print(str)

items = str.split(sep='\n')
for i, e in enumerate(items, 1):
    print(i, '. ', e.split(sep=' ')[0])

for i in range(1):
    print(i)
