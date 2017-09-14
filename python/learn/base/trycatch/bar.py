#!/usr/bin/python3
# -*- coding: utf-8 -*-


def bar ():
    """TODO: Docstring for bar .
    :returns: TODO

    """
    try:
        print("try")
    except Exception as e:
        raise
    else:
        # yes
        print("else")
    finally:
        print("finally")

bar()
