#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

def main():
    """
    3x + 6y − 5z = 12
     x − 3y + 2z = −2
     5x − y + 4z = 10

     3   6 -5     x     12
     1  -3  2  *  y  =  -2
     5  -1  4     z     10
    """

    # 使用矩阵方式
    A = np.matrix([[3,6,-5],[1,-3,2],[5,-1,4]])
    B = np.matrix([[12], [-2], [10]])
    XYZ = A ** (-1) * B
    print(XYZ)

    # 使用函数
    a = np.array([[3,6,-5],[1,-3,2],[5,-1,4]])
    b = np.array([[12], [-2], [10]])
    # 逆, 内积
    xyz = np.linalg.inv(a).dot(b)
    print(xyz)


if __name__ == "__main__":
    main()
