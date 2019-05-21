#!/usr/bin/python3
# -*- coding: utf-8 -*-


#  print(dir(dict))

d = { 'a' : 1, 'b' : 2, 'c' : 3 }

# setdefault()
print("-------------- ")
# 返回实际值
print(d.setdefault('a', 0))
print(d['a'])
print("-------------- ")

## 访问一个不存在的项 KeyError:
# print(d['w'])
if d.get('w', None):
    print('exist w')
else:
    print('not exist w')

for x, y in d.items():
    print(x, ':' , y)

print(d)
print(d['a'])
print(list(d))
print(list(d.items())) # 每一个name：value成为一个元组
print(list(d.keys()))
print(list(d.values()))
print(sorted(d.keys()))

d.pop('b')
print(d)
d.popitem() # ? 为什么少一项
print(d)

print(dict([('aa', 11), ('bb', 22), ('cc', 33)]))
print(dict(aaa = 111, bbb = 222, ccc = 333))
print({x:x**2 for x in (2, 3, 4)})

print("-------------- ")
d = {}
d[2,1] = 2
print(d) # result: {(2, 1): 2}


