#!/usr/bin/python3
# -*- coding: utf-8 -*-

class LeecoA(object):

    """Docstring for LeecoA. """

    def __init__(self):
        """TODO: to be defined1. """
        self._inner_var = 1
        self.__priv_var = 2  # 同双下划线的方法

    def public_call(self):
        print(" A public_call ")

    def _inner_call(self): # 约定成熟， 单下划线是内部使用的方法， 虽然可以外部调用， 但不建议
        print(" A _inner_call {}".format(self._inner_var))

    def __private_call(self):  # 双下划线 在方法字典中映射为_LeecoA__private_call, 从而实现不被覆盖
        print(" A __private_call {}".format(self.__priv_var))

class LeecoB(LeecoA):

    """Docstring for LeecoB. """

    def __init__(self):
        """TODO: to be defined1. """
        LeecoA.__init__(self)
        self._inner_var = 11  # 将会覆盖掉LeecoA中的该变量
        self.__priv_var = 22

    def public_call(self):
        print(" B public_call ")
        super().public_call()

    def _inner_call(self):
        print(" B _inner_call {}".format(self._inner_var))
        super()._inner_call()

    def __private_call(self):
        print(" B __private_call {}".format(self.__priv_var))
        super()._LeecoA__private_call() # 只用了演示， 调用不合理

a = LeecoA()
print(dir(a))
b = LeecoB()
print(dir(b))

print("-------------- ")

a.public_call()
b.public_call()

print("--------------")

a._inner_call()
b._inner_call()

print("-------------- ")

#  a.__private_call() # 私有化， 调用出错， 名字更改了
#  b.__private_call()

print("-------------- ")
a._LeecoA__private_call() 

# 只做演示
b._LeecoA__private_call() 
b._LeecoB__private_call() 
