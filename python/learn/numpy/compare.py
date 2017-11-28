#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("../base/wrap")
from mytimeit import timeit

import numpy as np

@timeit
def run_program1(attr, scalar):
    return attr * scalar

@timeit
def run_program2(attr, scalar):
    for i, val in enumerate(attr):
        attr[i] = val * scalar
    return attr

def main():
    arr1 = np.ndarray(1e7)
    arr2 = arr1.tolist() 
    print(type(arr1))
    print(type(arr2))

    run_program1(arr1, 1.1)
    run_program2(arr2, 1.1)


if __name__ == "__main__":
    main()
