#!/usr/bin/python3
# -*- coding: utf-8 -*-

def function(x, y, *args):
    print(x, y, args)

def function2(**kwargs):
    print(kwargs)

def _main(*args, **kwargs):
    print(args)
    print(kwargs)
    function(1, 2, 3, 4, 5)
    function2(a=1, b=2, c=3)


if __name__ == "__main__":
    a = {'a':1, 'b':{'bb':1}}
    _main(*a, **a)
