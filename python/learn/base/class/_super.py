#!/usr/bin/python
# -*- coding: utf-8 -*-


class A(object):
    def __init__(self):
        print("A")


# class B(A):
class B:
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        super().__init__()
        print("C")

    def doC(self):
        print("doC:", self.value)


class CC(C):
    def __init__(self):
        super(C, self).__init__()
        print("CC:")
        self.value = 100


class D(B, C):
    pass
    # def __init__(self):
    #     print("D")
    #     super().__init__()


cc = CC()
cc.doC()
# D()  # D里面没有，则找父类（从左往右），找到B
