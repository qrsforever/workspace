#! /usr/bin/python2.7
#coding:utf-8

def fun1(n):
    return [x for x in range(n)]

# print fun1(10)

def fun2(n):
    return [x**2 for x in range(n)]

# print fun2(4)

if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    if len < 2:
        exit(1)
    n = int(sys.argv[1])
    print fun1(n)
    print fun2(n)
