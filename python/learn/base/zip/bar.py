#!/usr/bin/python3
# -*- coding: utf-8 -*-

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

xyz = zip(x, y, z)

# xyz 是zip迭代对象, 如果调用了list, 再调用结果是不同的
print(list(xyz))
# output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

print("-------------- ")

print(list(xyz))
# output: []

print("-------------- ")

# 解压
xyz = zip(x,y,z)
print(list(zip(*xyz)))

print("-------------- ")

xyz = zip(x,y,z)
xs, ys, zs = xyz
print(xs)

print("-------------- ")

# 合并(维持3列)
# 方式1:
d1 = [[1,1,1], [2,2,2,2], [3,3]]
d2 = [[1,1], [2,2], [3,3,3]]
d1[0].extend(d2[0])
d1[1].extend(d2[1])
d1[2].extend(d2[2])
print(d1)

print("-------------- ")
# 方式2: 缺点zip会自动截取, 个数不对 (2 + 2 = 4)
d1 = [[1,1,1], [2,2,2,2], [3,3]]
d2 = [[1,1], [2,2], [3,3,3]]
z1 = zip(*d1)  # [(1,2,3), (1,2,3)]
print(list(z1))
z2 = zip(*d2)  # [(1,2,3), (1,2,3)]
print(list(z2))
z = list(z1) + list(z2)  # [(1,2), (1,2), (1,2), (1,2)]
d = zip(*z) # [(1,1,1,1), (2,2,2,2)]
print(list(d))

print("---------------")
print(d1)
print(d2)
print(list(zip(d1, d2)))
