#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

def test_save_load():# {{{
    """
    存储多个数组到文件中
    """
    a1 = np.arange(8)
    a2 = np.add.accumulate(a1)
    a3 = a1 + a2
    with open("/tmp/save_load.npy", "wb") as fw:
        np.save(fw, a1)
        np.save(fw, a2)
        np.save(fw, a3)

    with open("/tmp/save_load.npy", "rb") as fr:
        b1 = np.load(fr)
        b2 = np.load(fr)
        b3 = np.load(fr)
        # 再次np.load(r)会有异常

    print(a1, a2, a3)
    print(b1, b2, b3)
# }}}

def test_save_load2():# {{{
    """
    低级保存, 不保存数组的结构(shape,dtype)
    """
    arr = np.arange(12)
    arr.shape = (3, 4)
    print(arr, arr.shape, arr.dtype)

    arr.tofile("/tmp/arr.bin")
    arr2 = np.fromfile("/tmp/arr.bin")
    # 错误, 默认是float型
    print(arr2)
    arr3 = np.fromfile("/tmp/arr.bin", dtype=np.int64)
    # 错误, 一维的
    print(arr3)
    arr3.shape = (3, 4)
    # 正确
    print(arr3)
# }}}

def test_read_csv():# {{{
    """
    读取csv文件, 列类型不统一的处理
    """
    # loadtxt 对编码有个bug, 临时如下解决
    with open("./test.csv", encoding='latin1') as fp:
        arr = np.loadtxt(fp, dtype='S', delimiter=',') 
        print("arr.shape = " , arr.shape)
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                print(arr[i,j].decode('utf-8'))
        data = arr[1:,1:].astype(np.float) 
        print(data)

    with open("./test.csv", encoding='latin1') as fp:
        dt = np.dtype({
            'names':['name', 'age', 'weight', 'height'], 
            'formats':['S32', 'i', 'f', 'f']
            })
        # 如果列中数组类型不统一, 则返回所有列作为一维数据
        arr = np.loadtxt(fp, dtype=dt, delimiter=',', skiprows=1) 
        print("arr.shape = " , arr.shape)

        # 方法1 转置
        data = np.transpose(np.array([arr['age'], arr['weight'], arr['height']]))
        print("methd1:", data)

        # 方法2 
        data = np.zeros((3, 3))
        data[:,0] = arr['age']
        data[:,1] = arr['weight']
        data[:,2] = arr['height']
        print("method2:", data)

    # 方法3
    with open("./test.csv", encoding='latin1') as fp:
        arr = np.loadtxt(fp, delimiter=',', skiprows=1, usecols=(1,2,3))
        print(arr, arr.shape)
        
# }}}

def test_data_table():# {{{
    """
    unpack, NAN, MISSING, genfromtxt
    """
    arr = np.loadtxt("./data_table.txt", skiprows=1)
    print(arr, arr.shape)
    # unpack: 返回一个列独立数组
    c1, c2, c3 = np.loadtxt("./data_table.txt", skiprows=1, unpack=True)
    print(c1, c2, c3)

    # 如果文件中有NAN, 自动处理, 不会增加dtype类型
    arr = np.loadtxt("./data_table2.txt", skiprows=1)
    print(arr, arr.shape)

    # 如果skiprows=1,忽略
    arr = np.genfromtxt("./data_table3.txt", skip_header=1)
    print(arr, arr.shape)

    # 对特殊值进行填充 (每一列可以补充不同的值)
    arr = np.genfromtxt("./data_table3.txt", skip_header=1, 
            missing_values=('MISSING', 'MISSING', 'MISSING'),
            filling_values=(-999, -888, -777))
    print(arr, arr.shape)
# }}}

def main():
    test_save_load()
    test_save_load2() 
    test_read_csv()
    test_data_table()

if __name__ == "__main__":
    main()
