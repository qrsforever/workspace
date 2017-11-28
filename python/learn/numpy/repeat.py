#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

def main():
    """
    repeat: 对数组中的<<元素>>重复操作
    tile: 对<<整个>>数组进行复制拼接
    """
    arr = np.array([[1,2,3],[4,5,6]])
    # axis = 0, 对第1行重复1次, 对第2行重复2次
    arr1 = np.repeat(arr, (1, 2), axis=0)
    print(arr1)
    # axis = 1, 对第1,2列重复1次, 对第3列重复3次
    arr2 = np.repeat(arr, (1, 1, 3), axis=1)
    print(arr2)

    # 将整个数组, 行方向复制拼接2次, 列方向拼接复制2次
    arr3 = np.tile(arr, (2,2))
    print(arr3)
    arr4 = np.tile(arr, (1,2))
    print(arr4)
    pass

if __name__ == "__main__":
    main()
