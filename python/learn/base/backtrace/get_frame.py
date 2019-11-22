#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys  
import traceback


print(sys._getframe().f_lineno)


def get_cur_info():
    print(sys._getframe().f_code.co_filename)  # 当前文件名，可以通过__file__获得
    print(sys._getframe().f_code.co_name)  # 当前函数名
    print(sys._getframe().f_lineno) # 当前行号

get_cur_info()
