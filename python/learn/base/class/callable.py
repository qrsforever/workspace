#!/usr/bin/python3
# -*- coding: utf-8 -*-


class MyClass(object):

    """Docstring for MyClass. """

    def __init__(self):
        """TODO: to be defined1. """
        
    def __call__(self):
        print("__call_ called")
        pass

    def __getattr__(self, method):
        print("call", method)
        return lambda *args, **kwargs: 100

class MyClass2(object):
    def __delay_do(self, method, *args, **kwargs):
        print(" __delay_do")
        import time
        time.sleep(1)
        print(" __delay_do end")

    def __getattr__(self, method):
        print("call", method)
        return lambda *args, **kwargs: self.__delay_do(method, args, kwargs)

class MyClass3(object):
    def __init__(self):
        self.a = 1

    def __getattr__(self, method):
        def wrapper(*args, **kwargs):
            print("call", method, args, kwargs, self.a)
            import time
            time.sleep(1)
            return 10
        return wrapper

def function(f):
    """TODO: Docstring for function.

    :f: TODO
    :returns: TODO

    """
    print("callable: ", callable(f))
    f()


# function(MyClass())

# c = MyClass()
# print(c.add(1,1))

# c = MyClass2()
# print(c.add(1,1))

c = MyClass3()
print(c.add(1,1))
