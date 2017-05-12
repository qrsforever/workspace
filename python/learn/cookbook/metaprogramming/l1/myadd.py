#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("decorator1")
        return func(*args, **kwargs)

    print("decorator1.wrapper: ", end=" ")
    print(wrapper)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("decorator2")
        return func(*args, **kwargs)

    print("decorator2.wrapper: ", end=" ")
    print(wrapper)
    return wrapper

@decorator1
@decorator2
def myadd(x, y):
    print("myadd ", end=" ")
    print(myadd)
    return x + y

print("------1-------- ")
print(myadd) # decorator2.wrapper
print(myadd.__wrapped__)  # decorator1.wrapper
print(myadd.__wrapped__.__wrapped__)  # decorator1.wrapper
print(myadd.__wrapped__(1,2))
print(myadd(1,2))
print("------2-------- ")


# 原理分析： 越靠近原函数优先包装

def myadd2(x, y):
    print("myadd2 ", end=" ")
    print(myadd2)
    return x + y

myadd2 = decorator2(myadd2) # decorator2.wrapper
print("-------------- ")
print(myadd2.__wrapped__)
print(myadd2.__wrapped__(1,2)) # 得到就是myadd2函数本身
myadd2 = decorator1(myadd2) # decorator1.wrapper
print("-------------- ")
print(myadd2.__wrapped__)
print(myadd2.__wrapped__(1,2))

print(myadd2(1, 2))
