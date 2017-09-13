#!/usr/bin/python3
# -*- coding: utf-8 -*-


class MyClass(object):

    """Docstring for MyClass. """

    def __init__(self):
        """TODO: to be defined1. """
        
    def __call__(self):
        pass


def function(f):
    """TODO: Docstring for function.

    :f: TODO
    :returns: TODO

    """
    print("callable: ", callable(f))
    pass


function(MyClass())
