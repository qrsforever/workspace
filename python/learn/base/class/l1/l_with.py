#!/usr/bin/python3
# -*- coding: utf-8 -*-

class LeecoOpenFile(object):

    """Docstring for LeecoOpenFile. """

    def __init__(self, file):
        """TODO: to be defined1. """
        self._file = file 
        self._fp = None

    def __enter__(self):
        print("__enter__")
        if self._fp is not None:
            RuntimeError("File already open")
        try:
            self._fp = open(self._file, 'rt')
        except Exception as e:
            print(str(e))
        return self._fp

    def __exit__(self, exec_ty, exec_val, tb): # 异常类型， 异常值， 追溯信息
        print("__exit__")
        self._fp.close()
        self._fp = None


a = LeecoOpenFile('./l_format.py')

with a as fp:
    print("Do something")


print("-------------- ")


class LeecoOpenFile(object):

    """Docstring for LeecoOpenFile. """

    def __init__(self, file):
        """TODO: to be defined1. """
        self._file = file 
        self._fps = []  # 递归调用with的实现

    def __enter__(self):
        try:
            fp = open(self._file, 'rt')
        except Exception as e:
            print(str(e))
        print("__enter__ {}".format(fp.__hash__))
        self._fps.append(fp)
        return fp

    def __exit__(self, exec_ty, exec_val, tb): # 异常类型， 异常值， 追溯信息
        fp = self._fps.pop()
        print("__exit__{}".format(fp.__hash__))
        fp.close()


b = LeecoOpenFile('./l_format.py')

with b as fp1:
    print("Do something: fp1")
    with b as fp2:
        print("Do something: fp2")
