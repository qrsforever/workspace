#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

def cacShannonEntropy(dataSet):# {{{
    """
    计算香浓熵(信息熵: 信息的期望值)

    Parameters
    ----------
    dataSet: 最后一列为标签类别
             混合的分类越多, 熵越大
    Returns
    -------
    shannonEnt: 信息期望

    Notes
    -----
    符号信息:
    事物可划分为多个分类(符号)， 
    每个符号携带一定信息
    信息的大小与选择这个分类的概率p的有关.
    
    TODO:
    数据很大时, 概率会很小, 为了方便表达信息使用-math.log(p, 2)
    概率越小, 信息值越大

    熵： 
     　 所有分类可能值的信息的期望
        ? 度量数据集的无序程度　 

    """
    
    dataLen = len(dataSet)
    groups = { }
    for featVec in dataSet:
        label = featVec[-1]
        groups[label] = groups.get(label, 0) + 1

    shannonEnt = 0.0
    for label, count in groups.items():
        prob = count / dataLen
        # 信息定义:  -math.log(prob, 2), 定义如此, 不要纠结
        # 再*prob --> 所有求和就是信息期望
        # 如果'A'概率为1/8 ---> -log(1/8,2) = log(8,2), 概率越小, 信息越大
        shannonEnt += -math.log(prob, 2) * prob

    return shannonEnt
# }}}

def majorityCnt(classList):# {{{
    """
    返回出现频数最多的标签类 
    
    Parameters
    ----------
    classList: 包含类标签的List集合
    
    Returns
    -------
    label: 出现频数最多的标签类 
    
    Notes
    -----
    
    """
    
    records = {}
    for it in classList:
        records[it] = records.get(it, 0) + 1

    sortedRecords = sorted(records.items(), key=lambda it: it[1], reverse=True)
    return sortedRecords[0][0]
# }}}

def splitDataSet(dataSet, axis, value):# {{{
    """
    按给定轴axis对应的值(特征)value划分数据
    划分的结果不再包含axis（特征） --- 抽取子集
    
    Parameters
    ----------
    axis: 坐标轴(纬度) --> 特征
    value: 轴上的数据值
    
    Returns
    --------
    splitVec: 由axis和value决定的下来的数据
                (不再包含该axis上的数据)
    
    """
    newData = []
    for featVec in dataSet:
        if featVec[axis] == value:
            splitVec = featVec[:axis] 
            splitVec.extend(featVec[axis+1:])
            newData.append(splitVec)
    return newData

# }}}

def chooseBestFeatureToSplit(dataSet):# {{{
    """
    选择最好的特征（列）进行分类，分别划分每个特征（列）
    计算划分后的信息熵（唯一特征值对应熵的和）
    信息增益：划分前后熵的差

    什么是最好的: 选择的特征划分后, 使信息增益最大
    
    Parameters
    ----------
    dataSet: 数据集, 本代码有个约定，最后一列是类别，不作为特征
    
    Returns
    -------
    使信息增益最大的特征(列)
    
    Notes:
    -----
    信息增益: 
    1. 将无序的数据变得更加有序
    2. 使用信息论量化度量信息的内容
    3. 划分前后信息发生的变化-->信息增益 (熵的减少或数据无序度的减少)

    TODO:
    一个极端的理解：
    如果axis = 0, 唯一特征值(F1, F2, F3)　
    F1 ---> Ｃ1 (无其他分类) ---> 熵为０ --> 信息增益＝划分之前的熵
    F2 ---> Ｃ2 (无其他分类) ---> 熵为０ --> 信息增益＝划分之前的熵
    F3 ---> Ｃ3 (无其他分类) ---> 熵为０ --> 信息增益＝划分之前的熵
    那么基本上axis的特征可以决定分类了。
    
    """

    featNum = len(dataSet[0]) - 1
    dataCount = len(dataSet)
    # 划分之前的熵
    baseShannonEnt = cacShannonEntropy(dataSet)

    currentMaxGain = 0.0 # 记录当前信息增量最大值
    featIndex = -1 # 记录信息增益最小时的特征列i

    # 求每个特征划分后的熵
    for i in range(featNum):
        featValues = [ d[i] for d in dataSet ]
        # 特征值去重(保证唯一的最好方法set)
        featValues = set(featValues)
        featShannonEnt = 0.0
        for value in featValues:
            newData = splitDataSet(dataSet, i, value)
            prob = len(newData) / float(dataCount)
            # (唯一)每个特征值对应熵的期望
            featShannonEnt += prob * cacShannonEntropy(newData)
        currentGain = baseShannonEnt - featShannonEnt
        if currentGain > currentMaxGain:
            currentMaxGain = currentGain
            featIndex = i
    return featIndex

# }}}

def createTree(dataSet, labels):# {{{
    """
    递归构建决策树
    
    Parameters
    ----------
    dataSet: 数据集, 约定最后一列为分类
    labels: 特征对应的标签名字(用来显示, 非必须)
    
    Returns
    -------
    myTree:
    
    Notes
    -----
    
    """

    # 构建树的终止条件(2个)
    # 虽然特征还有剩余要split的, 但是分类相同, dataSet的熵为0(1)
    classList = [d[-1] for d in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # 没有特征要split, 但是分类还有几个(2)
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    # 选择一个最好的特征去split数据集
    featIndex = chooseBestFeatureToSplit(dataSet)
    featLabel = labels[featIndex] 
    myTree = {featLabel: {}}
    del(labels[featIndex])

    # 该特征里按特征值分组
    featValues = [d[featIndex] for d in dataSet]
    featValues = set(featValues)
    # 按照特征值分组, 每个组对应一个dataSet子集
    for value in featValues:
        subLabels = labels[:]
        # 使用子集继续构建tree
        myTree[featLabel][value] = createTree(splitDataSet(dataSet, featIndex, value), subLabels)

    return myTree
# }}}

def createDataSet(s=0):# {{{
    """
    生成测试数据
    """
    if s == 2:
        dataSet = [
                [1, 2, 'A'],
                [3, 4, 'B'],
                [1, 3, 'E'],
                [3, 6, 'C'],
                [5, 7, 'D'],
                [4, 9, 'B'],
                [4, 3, 'D'],
                [8, 1, 'A']]
        labels = ['first', 'second']
    elif s == 1:
        """
        第2特征:
        1 --> A
        2 --> B
        3 --> C
        """
        dataSet = [
                [1, 1, 'A'],
                [2, 2, 'B'],
                [0, 3, 'C'],
                [1, 3, 'C'],
                [0, 2, 'B'],
                [1, 1, 'A'],
                [2, 2, 'B'],
                [1, 1, 'A']]
        labels = ['first', 'second']
    else:
        dataSet = [
                [1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
        labels = ['no surfacing','flippers']

    return dataSet, labels
# }}}

def main():
    dataSet, labels = createDataSet()
    #  print(cacShannonEntropy(datqaSet))
    #  print(splitDataSet(dataSet, 1, 3))
    #  print(chooseBestFeatureToSplit(dataSet))
    #  print(majorityCnt(['a', 'b', 'a', 'a', 'b', 'c', 'c']))
    tree = createTree(dataSet, labels)
    print(tree)


if __name__ == "__main__":
    main()
