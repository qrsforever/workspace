#!/usr/bin/python3
#coding:utf-8

from itertools import zip_longest

print(dir(list))

l = [x for x in range(10)]

print(l.__class__)

l.append('d')
l.insert(0, 0)
l.insert(3, 'a')
print(l)
print(l.count('a'))
l.pop() # 最后一个
print(l)
l.pop(0)
print(l)
l.remove('a')
print(l)
l.reverse()
print(l)
l.sort(reverse=True)
for x in l:
    print(x, end=',')


print("-------------- enumerate")

for i, x in enumerate(l, 0):
    print(i, x)

print("-------------- zip")

a = [1, 2, 3]
b = [4, 5, 6, 7]
for x, y in zip(a, b):
    print(x, y) # 7 not output

print("-------------- zip_longest")

for x, y in zip_longest(a, b, fillvalue=0):
    print(x, y) 


print("-------------- ")

data = [1, 2 , 3, 4, 5]

print(data[:-2]) # 1,2,3
print(data[-1])  # 5
print(data[-2])  # 4
