#!/usr/bin/python3
# -*- coding: utf-8 -*-

import traceback

def _stack_tuple_to_function_line_filename(stackTuple):
    filename = stackTuple[0]
    linenumber = stackTuple[1]
    funcname = stackTuple[2]
    codeline = stackTuple[3]
    return 'func: %s\nline: %d\nfile: %s\n%s' % (funcname, linenumber, filename, codeline)

def get_filename_function_line(limit=1):  # limit = 1 表示抽取该函数调用者的位置，注意输入到extract_stack中的limit=limit+1
    stackTuple = traceback.extract_stack(limit=limit + 1)[0]
    return _stack_tuple_to_function_line_filename(stackTuple)

def print_with_pos(*args, **kwargs):  # 输出语句，同print，只是之后会再输出位置信息
    print(*args, **kwargs)
    print('%s' % get_filename_function_line(limit=2))


def f1():
    print_with_pos("Hello World")

def f2():
    return f1()

def f3():
    return f2()

def main():
    f3()

if __name__ == "__main__":
    main()
