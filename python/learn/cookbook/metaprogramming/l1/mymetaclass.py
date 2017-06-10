#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Singleton(type):
    def __init__(self, *args, **kwargs):
        print("Singleton.__init__")
        self._instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("Singleton.__call__")
        if self._instance is None:
            print("new instance")
            self._instance = super().__call__(*args, **kwargs)
        return self._instance

class Foo(metaclass=Singleton):
    def __init__(self, *args, **kwargs):
        print("Foo.__init__")

class A:
    def __init__(self, *args, **kwargs):
        print("A.__init__")
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("A.__call__")
        return super().__call__(*args, **kwargs)


# B 继承 A， 不会调用A的__call__函数
class B(A):
    def __init__(self, *args, **kwargs):
        print("B.__init__")
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("B.__call__")


a = Foo()
b = Foo()

c = B()
