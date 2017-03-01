#!/usr/bin/python2.7

def fib(n):
    """
    TODO
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b

    return result

f = fib
print (f.__doc__)
print f(100)
