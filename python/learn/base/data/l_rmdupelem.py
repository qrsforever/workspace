#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
set 可以去掉重复的， 但是原有元素顺序改变了
"""
a = [3, 1, 2, 1, 2, 1, 2, 2]
print(a, set(a))
b = (3, 1, 2, 1, 2, 1, 2)
print(a, set(b))
c = { 'a': 1, 'b': 2, 'a': 1 }
print(c, set(c))

"""
自己实现生成器， 保证顺序, 去掉重复的
"""
def rmdupelem(items):
    s = set()
    for i in items:
        if i not in s:
            yield i
            s.add(i)

print(list(rmdupelem(a)))
print(list(rmdupelem(b)))
