#!/usr/bin/python
# -*- coding: utf-8 -*-

class AA(object):

    """Docstring for AA. """

    def __init__(self, b=None, a=0.4):
        self.b = b
        self.a = a
        print(a, b)
        

dt = {'b':[], 'a':1.0}

aa = AA(**dt)
