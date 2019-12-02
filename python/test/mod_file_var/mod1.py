#!/usr/bin/python3
# -*- coding: utf-8 -*-

from globalvar import DICT_VAR
import otherfile
from cls import Cls2

print(DICT_VAR)

otherfile.test()

DICT_VAR['a'] = 100
DICT_VAR['b'] = 100
DICT_VAR['f'] = Cls2

print(DICT_VAR)

otherfile.test()
