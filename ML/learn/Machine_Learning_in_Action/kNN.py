#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pylab as plt

def knnClassify(inX, dataSet, labels, k = 3):# {{{
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
# }}}

def createDataSet():# {{{
    """
            1.0     1.1     A
            1.0     1.0     A
            0.0     0.0     B
            0.0     0.1     B
    """
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels
# }}}

def simpleTest():# {{{
    inXs = np.array([[0.5, 0.5], [0.2, 0.2], [0.7, 0.7]])
    dataSet, labels = createDataSet()
    for i in range(inXs.shape[0]):
        label = knnClassify(inXs[i], dataSet, labels)
        print(inXs[i], ":", label)
# }}}

def file2matrix(filename):# {{{
    # 以字符串类型读取文件, 方便二维处理
    fullMatrix = np.loadtxt(filename, dtype='S')
     
    # 提取Data
    dataMatrix = fullMatrix[:, 0:3].astype(np.float)
    # 提取Labels (datingTestSet.txt里面是字符串)
    labelsVec = fullMatrix[:, -1].astype(np.int)
    
    return dataMatrix, labelsVec
# }}}

def autoNormalize(dataSet):# {{{
    """
    矩阵归一化

    Parameters
    ----------
    dataSet : ndarray

    """
    # 每一列最小/大值
    minValues = dataSet.min(axis=0)
    maxValues = dataSet.max(axis=0)
    rangeValues = maxValues - minValues

    dataNorm = dataSet - np.tile(minValues, (dataSet.shape[0],1))
    # 特征值相除, 不是矩阵相除
    dataNorm = dataNorm / np.tile(rangeValues, (dataSet.shape[0], 1))

    return dataNorm, rangeValues
    # }}}

def datingClassTest():# {{{
    """
    约会问题
    每年飞行里程数, 玩游戏百分比, 冰淇淋公升数,  喜欢类型(1,2,3)
    """
    dataMatrix, labelsVec = file2matrix("./machinelearninginaction/Ch02/datingTestSet2.txt")
    dataMatrix, rangeValues = autoNormalize(dataMatrix)

    roRate = 0.10
    itemCount = dataMatrix.shape[0]
    testCount = int(roRate * itemCount)

    errCount = 0
    for i in range(testCount):
        result = knnClassify(
                dataMatrix[i,:], 
                dataMatrix[testCount:itemCount,:], 
                labelsVec[testCount:itemCount])
        print("%d. [%d] vs [%d]" % (i, result, labelsVec[i]))
        if result != labelsVec[i]:
            errCount += 1
    print("errRate = ", errCount / testCount)

    if errCount > 10:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(dataMatrix[:,1], dataMatrix[:,2], s=15.0*labelsVec, c=15.0*labelsVec)
        plt.show()
# }}}

def image2Vector(imgfile):# {{{
    """
    image to vector
    """
    vect = np.zeros((1, 1024))
    with open(imgfile, 'r') as fr:
        data = fr.readlines()
        for i in range(32):
            for j in range(32):
                vect[0, i*32 + j] = int(data[i][j])
    return vect
# }}}

def digitClassTest():# {{{
    """
    手写数字测试
    """
    trainingDigitsDir = "machinelearninginaction/Ch02/trainingDigits"
    testDigitsDir = "machinelearninginaction/Ch02/testDigits"

    def _parseLabel(filename):
        """
        解析label, 0_11.txt ---> 0
        """
        return int(filename.split('_')[0])

    # 训练矩阵
    trainingFileList = os.listdir(trainingDigitsDir)
    trainFilesCount = len(trainingFileList)
    trainMatrix = np.zeros((trainFilesCount, 1024), dtype=int)
    trainLabels = []
    for i in range(trainFilesCount):
        trainFile = trainingFileList[i]
        trainPath = os.path.join(trainingDigitsDir, trainFile)
        trainMatrix[i] = image2Vector(trainPath)
        trainLabels.append(_parseLabel(trainFile))

    # 测试
    errCount = 0
    for i, testFile in enumerate(os.listdir(testDigitsDir)):
        testPath = os.path.join(testDigitsDir, testFile)
        testVect = image2Vector(testPath)
        retval = knnClassify(testVect, trainMatrix, trainLabels, k = 3)
        relval = _parseLabel(testFile)
        #  print("%d. [%d] vs [%d]" % (i, retval, relval))
        if retval != relval:
            errCount += 1

    print("errRate: %d/%d = %.6f" % (errCount, i, errCount / i))
# }}}

def main():
    simpleTest()
    datingClassTest()
    digitClassTest()

if __name__ == "__main__":
    main()
