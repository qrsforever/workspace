#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

def test1():
    """
    """

    arr = np.loadtxt("./somefile.txt", dtype={'names': ('ID', 'Result', 'Type'), 'formats': ('S4', 'f4', 'i2')})
    print(arr)
    print(arr.dtype)
    print(arr['ID'])
    arr['ID'] = [b'1111', b'2222']
    print(arr)

    # error ??
    #  np.savetxt("./somenewfile.txt", arr)

def main():
    test1()

if __name__ == "__main__":
    main()
