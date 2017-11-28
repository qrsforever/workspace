#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

def test1():
    """
    array and data typing
    """
    l = [1, 2, 3, 4, 5]

    d0 = np.array(l)
    print(type(d0), d0)

    d1 = np.zeros(5)
    print(type(d1), d1)

    d2 = d1.astype(int) + 1
    print(type(d2), d2)

    d3 = np.ones((3, 3), dtype=np.float)
    print(d3)

    d4 = np.arange(100)
    print(d4)

    d5 = np.linspace(1, 10, num=20, endpoint=True, retstep=False)
    print(d5)

    d6 = np.logspace(1, 10, num=20, endpoint=True, base=10.0)
    print(d6)

    d7 = d4.reshape((10, 10))
    print(d7)

    d8 = d7.reshape((5, 20))
    print(d8.shape)

def test2():
    """
    record array
    """
    l = [(1, 1.0, 'Hello'), (2, 2.0, 'World')]
    d1 = np.zeros((2,), dtype=('i4, f4, a10'))
    d1[:] = l
    print(d1, d1.dtype.names, d1['f1'])
    d1.dtype.names = ( 'Integers', 'Floats', 'String' )
    print(d1['Integers'])

    #  col1 = np.arange(2) + 1
    #  col2 = np.arange(2).astype(np.float32)
    #  col3 = ['Hello', 'World']
    #  toadd = zip(col1, col2, col3)
    #  error! ??
    #  d1[:] = toadd

def test3():
    """
    indexing and slicing
    """
    alist = [[1,2], [3,4], [5,6]]
    print(alist, alist[1][0])
    arr = np.array(alist) 
    print(arr, arr[1,0])
    # 所有行列
    print(arr[::])
    # 前2行, 后2行
    print(arr[:2], arr[-2:])
    # 访问第2列 
    print(arr[:, 1])
    # 访问0到2列, 不包括第2列
    print(arr[:, 0:2])

    # 一维
    #  arr = np.arange(10)
    arr = np.array([5,4,6,9,8,7,3,1,2])
    print(arr)
    # 数组中数值大于5的index
    index = np.where(arr > 5)
    print(index)
    # 删除index中指定的元素
    arr = np.delete(arr, index, axis=None)
    print(arr)

    #  # 多维 TODO 失败
    #  arr = np.array([[3, 5, 6], [4, 2, 7]])
    #  print(arr)
    #  index = np.where(arr > 4)
    #  print(index)
    #  arr = np.delete(arr, index, axis=None)
    #  print(arr)



def main():
    #  test1()
    print("-------------- ")
    #  test2()
    print("-------------- ")
    test3()



if __name__ == "__main__":
    main()
