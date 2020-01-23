#!/usr/bin/python3
# -*- coding: utf-8 -*-

from globalvar import DICT_VAR


def test():
    print("other", DICT_VAR)
    DICT_VAR['f']().test()
