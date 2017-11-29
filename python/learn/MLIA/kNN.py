#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt

def knnClassify(inX, dataSet, labels, k = 3):
    """
    KNN k-邻近算法
    """
    # 将输入向量inX转换(复制拼接)为矩阵和dataSet的shape相同
    dataSetSize = dataSet.shape[0]
    inMatrix = np.tile(inX, (dataSetSize, 1))

    # 欧几里得计算距离
    sqSumDistance = np.sum((inMatrix - dataSet)**2, axis=1)
    distances = sqSumDistance ** 0.5

    # 排序, 真正元素并没有变动, 只是对index进行记录
    sortedDistances = distances.argsort()

    # 查看前k个向量属于哪个类
    records = {}
    for i in range(k):
        label = labels[sortedDistances[i]]
        records[label] = records.get(label, 0) + 1
    #  print(records)

    # 对records排序 (k个中哪一类最多)
    sortedRecords = sorted(records.items(), key=lambda d: d[1], reverse=True)
    return sortedRecords[0][0]

def createDataSet():
    """
            1.0     1.1     A
            1.0     1.0     A
            0.0     0.0     B
            0.0     0.1     B
    """
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def simpleTest():
    inXs = np.array([[0.5, 0.5], [0.2, 0.2], [0.7, 0.7]])
    dataSet, labels = createDataSet()
    for i in range(inXs.shape[0]):
        label = knnClassify(inXs[i], dataSet, labels)
        print(inXs[i], ":", label)

def file2matrix(filename):
    # 以字符串类型读取文件, 方便二维处理
    fullMatrix = np.loadtxt(filename, dtype='S')
    # 提取Data
    dataMatrix = fullMatrix[:, 0:3].astype(np.float)
    # 提取Labels (datingTestSet.txt里面是字符串)
    labelsVec = fullMatrix[:, -1]
    return dataMatrix, labelsVec

def datingClassTest():
    dataMatrix, labelsVec = file2matrix("./machinelearninginaction/Ch02/datingTestSet2.txt")
    fig = plt.figure()

def main():
    #  simpleTest()
    datingClassTest()

if __name__ == "__main__":
    main()
