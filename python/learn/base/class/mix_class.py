#!/usr/bin/python3
# -*- coding: utf-8 -*-

class CC1(object):

    """Docstring for CC1. """

    def __init__(self):
        """TODO: to be defined1. """

    def cc1_method(self):
        print(" cc1_method ")


# 这个类调用了CC1里面的方法, CC1与CC2并没有关系
class CC2(object):

    """Docstring for CC2. """

    def __init__(self):
        """TODO: to be defined1. """
        
    def cc2_method(self):
        self.cc1_method()
        print(" cc2_method ")

class CC3(CC1, CC2):

    """Docstring for MyClass. """

    def __init__(self):
        """TODO: to be defined1. """
         
    def cc3_method(self):
        self.cc2_method()

c = CC3()
c.cc3_method()

# result:
# cc1_method 
# cc2_method 

