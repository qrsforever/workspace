#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functools import wraps
from time import clock

# import timeit
# time = timeit.timeit(stmt=myfun, number=1)

def timeit(func):
    @wraps(func)
    def _timeit(*args, **kwargs):
        start = clock()
        result = func(*args, **kwargs)
        end = clock()
        print("Time cost: ", end - start)
        return result

    return _timeit

@timeit
def main():
    import math
    for i in range(1, 100):
        for j in range(1, 100):
            math.pow(i, j)
            

if __name__ == "__main__":
    main()
