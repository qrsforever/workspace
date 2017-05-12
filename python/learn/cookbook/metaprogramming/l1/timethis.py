#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time 
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result 

    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

countdown(10000)


# 原理: @timethis 对元函数countdown进行封装

def countdown2(n):
    while n > 0:
        n -= 1

countdown2 = timethis(countdown2)
countdown2(10000)
