#!/usr/bin/python2.7
#coding:utf-8

def a_fun(arg0, arg1 = "n1", arg2 = 100):
    """
    a_fun test
    """
    print arg0, arg1, arg2

a_fun(arg0=1)
a_fun(2, "m1")
a_fun(3, "m1", "200")
a_fun(4, arg2 = 400)
a_fun(5, arg1 = 600)

def b_fun(args):
    """
    b_fun 参数为元组本身
    """
    for arg in args:
        print arg,
    print ''

args = [2, 4, 6]
b_fun(args)

def c_fun(*args):
    """
    c_fun 使用元组变参
    """
    for arg in args:
        print arg,
    print ''

c_fun(1, 3, 5)
c_fun(*args)

def d_fun(**args):
    """
    d_fun 使用字典变参
    """
    keys = args.keys();
    for k in keys:
        print k, "=", args[k]

dicts = {"a":"1", "b":"2"}
d_fun(**dicts)

def e_fun(arg0, *arg1, **arg2):
    """
    e_fun 参数顺序(关键参数>元组>字典)
    """
    print arg0, arg1, arg2

e_fun("0-0", "1-1", "1-2", a21="2-1", a22="2-2")
