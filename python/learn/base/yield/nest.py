#!/usr/bin/python3
# -*- coding: utf-8 -*-

def bar():
    for i in range(1, 10):
        print("----bar-----")
        yield i


def foo():
    for i in bar():
        print("----foo-----")
        yield i

def jar():
    for i in foo():
        print("----jar-----")
        yield i

def tar():
    for i in jar():
        print("----tar-----")
        yield i

if __name__ == "__main__":
    f = tar()
    print("----m1-----")
    print(f.send(None))
    print("----m2-----")
    print(f.send(None))
    print("----m3-----")

    import time
    time.sleep(100)
