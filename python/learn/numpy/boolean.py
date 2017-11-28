#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as rand

def test1():
    """
    & | 布尔运算
    """
    arr = np.zeros((16, 16)) + 3
    # 从第4行(列)到倒数第4行(列)
    arr[4:-4, 4:-4] = 6
    arr[7:-7, 7:-7] = 9
    #  print(arr)

    index1 = arr > 2
    index2 = arr < 6
    compound_index = index1 & index2
    compound_index = (arr > 3) & (arr < 9)
    arr2 = np.copy(arr, order='K')
    arr2[compound_index] = 0
    print(arr2)

    compound_index = (arr == 9) | (index1 & index2)
    arr3 = np.copy(arr)
    arr3[compound_index] = 0
    print(arr3)

def test2():
    """
    随机处理数据
    """
    # 返回高斯分布(0, 1)的一个样本
    arr = rand.randn(100)
    print(arr)
    # 采集数值大于0.2的子集
    index = arr > 0.2
    res = arr[index]
    # 子集中的数据平方减2
    res = res ** 2 - 2
    # 放回去
    arr[index] = res
    print(arr)

def main():
    test1()
    test2()

if __name__ == "__main__":
    main()
