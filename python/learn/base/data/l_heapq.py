#!/usr/bin/python3
#coding:utf-8

import heapq

print(dir(heapq))

a = [4, 3, 6, 9, 10]
print(heapq.heappop(a))
print(a[-1])

print(heapq.nlargest(2, a), heapq.nsmallest(2, a))
print(heapq.heapify(a))
