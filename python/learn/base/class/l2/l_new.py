#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  class A(): # python3 默认每个类都继承object 
class A(object):
    """
    1. 在类准备将自身实例化时调用
    2. 属于类的静态方法(即使没有被加上静态方法装饰器)
       cls: 即将被实例化的类 
       *args **kwargs: 多个参数和多个命名参数
       有返回值(类实力)， 先于__init__被调用， 然而__init__没有返回值
    """
    def __new__(cls, *args, **kwargs):
        print("call A.__new__()")
        kwargs['i'] = 4  # 在这里修改或增加数据是不影响__init__的参数的。
        print(args, kwargs)
        #  object = super(A, cls).__new__(cls, *args, **kwargs) # 这种写法在pytho3报错
        object = super(A, cls).__new__(cls)
        return object

    """
    self 实际上就是__new__的返回值
    """
    def __init__(self, *args, **kwargs):
        print("call A.__init__()")
        print(args, kwargs)
        super(A, self).__init__() # 在python3可以省略参数 super().__init__()

print(type(A(0, x=1,y=2,z=3)))

print("-------------- ")

class B(object):
    """Docstring for B. """
    def __new__(cls):
        print("B.__new__()")
        print("B: " + cls.__doc__)
        return float() # 随便返回一种类型， 注意type(b)的值

    def __init__(self):
        print("B.__init__()")  # 永远不会走到这

print(type(B()))

print("-------------- ")

class C(B):
    """Docstring for C. """
    def __new__(cls):
        print("C: " + cls.__doc__)
        o = super(C, cls).__new__(cls) #  o = super().__new__(cls)
        print("call C.__new__()")
        return o

    def __init__(self):
        print("Call C.__init__()")
        super(C, self).__init__()

print(type(C()))

#  call A.__new__()
#  (0,) {'i': 4, 'x': 1, 'y': 2, 'z': 3}
#  call A.__init__()
#  (0,) {'x': 1, 'y': 2, 'z': 3}
#  <class '__main__.A'>
#  --------------
#  B.__new__()
#  B: Docstring for B.
#  <class 'float'>
#  --------------
#  C: Docstring for C.
#  B.__new__()
#  B: Docstring for C.
#  call C.__new__()
#  <class 'float'>

