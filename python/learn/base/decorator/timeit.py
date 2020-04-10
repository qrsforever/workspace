#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functools import wraps
import time


def timeitx(func):
    @wraps(func)
    def timed(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print('"{}" took {:.3f} ms to execute\n'.format(func.__name__, (te - ts) * 1000))
        return result 
    return timed


@timeitx
def test(a):
    time.sleep(a)


test(1)
