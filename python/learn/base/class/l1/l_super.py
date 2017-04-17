#!/usr/bin/python3
# -*- coding: utf-8 -*-


# 难以理解的super()

class LeecoBase(object):

    """Docstring for LeecoBase. """

    def __init__(self):
        """TODO: to be defined1. """
        print("LeecoBase __init__")
        super().__init__()

    def callBase(self):
        print("LeecoBase callBase")


class LeecoA(LeecoBase):

    """Docstring for LeecoA. """

    def __init__(self):
        """TODO: to be defined1. """
        super().__init__()
        print("LeecoA __init__") 

    def callA(self):
        print("LeecoA callA")

    # 难以理解
    def callB_from_A(self):
        print("LeecoA callB_from_A")
        super().callB()

class LeecoB(LeecoBase):

    """Docstring for LeecoB. """

    def __init__(self):
        """TODO: to be defined1. """
        super().__init__()
        print("LeecoB __init__") 
    
    def callB(self):
        print("LeecoB callB")


class LeecoC(LeecoA, LeecoB):

    """Docstring for LeecoC. """

    def __init__(self):
        """TODO: to be defined1. """
        #  LeecoA.__init__(self)
        #  LeecoB.__init__(self)
        super().__init__()
        print("LeecoC __init__")

# 打印出继承类顺序列表
print(LeecoC.__mro__)

print("-------------- ")

l = LeecoC()
l.callA()
l.callB()
l.callBase()

print("-------------- ")
a = LeecoA()
#  a.callB_from_A() # 报错： super 对象么有 callB 属性
l.callB_from_A() # 正确： 混类

# 建议： LeecoC这样的子类把所有接口列出实现
