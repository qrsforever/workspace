#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

def loadDataSet():# {{{
    """
    斑点狗的评论条目
    """
    postingList=[
            ['my', 'dog', 'has', 'flea', \
                    'problems', 'help', 'please'],
            ['maybe', 'not', 'take', 'him', \
                    'to', 'dog', 'park', 'stupid'],
            ['my', 'dalmation', 'is', 'so', 'cute', \
                    'I', 'love', 'him'],
            ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
            ['mr', 'licks', 'ate', 'my', 'steak', 'how',\
                    'to', 'stop', 'him'],
            ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1] #1 is abusive, 0 not
    return postingList,classVec
# }}}

def generateVocabList(dataSet):# {{{
    """
    将dataSet中所有词汇集合一起(不重复)
    """
    vocabuSet = set([]) 
    for data in dataSet:
        vocabuSet = vocabuSet | set(data)
    return list(vocabuSet)
# }}}

def setOfWord2Vec(vocabuList, documents):# {{{
    """
    将参数documents中的单词映射到0,1的向量中
    单词转换为数字

    词集转换: 没有重复的单词
    """
    vecs = [0]*len(vocabuList)

    for word in documents:
        try:
            idx = vocabuList.index(word)
            vecs[idx] = 1
        except ValueError as e:
            print(e)
    return vecs
# }}}

def bagOfWord2Vec(vocabuList, documents):# {{{
    """
    词袋转换: 有重复的单词
    """
    vecs = [0]*len(vocabuList)

    for word in documents:
        try:
            idx = vocabuList.index(word)
            vecs[idx] += 1
        except ValueError as e:
            print(e)
    return vecs
# }}}

def trainingNaiveBayes(trainMatrix, trainCategory):# {{{
    """
    训练朴素贝叶斯 (这个实例比较简单: 特征值(0,1), 分类(0,1))  
    实际应用中某一个特征对应L个值, 有K个分类,  M维特征向量, N条数据

    计算某一特征值在某一分类下的概率, 本示例特征值就是0,1

    朴素: 特征条件独立
        p(w1,w2...|c) = p(w1|c)p(w2|c)...
        w1,w2是特征 

    Parameters
    ----------
    trainMatrix: 特征向量矩
    trainCategory: 特征向量对应的类别
    
    Returns
    -------
    pVectC0: 分类C=0对应dataset, 词条概率向量 (条件概率向量)
    pVectC1: 分类C=1对应dataset, 词条概率向量 (条件概率向量)
    pAbusive: 辱骂, 恶语在dataset中所占比例 (先验概率)
        (因为只有2个类, 返回一个即可)
    
    Notes
    -----
    每个分类下, 词条(特征向量)的概率


    """
    # 数据条目
    N = len(trainCategory)
    # 特征向量的维度
    M = len(trainMatrix[0])
    # 分类为1(Abusive)的个数
    K = sum(trainCategory)
    pAbusive = K / float(N)

    # 用来记录C0,C1分类中对应所有词条的频数 
    matrixC0 = np.ones(M) # (拉普拉斯平滑)
    matrixC1 = np.ones(M) # (拉普拉斯平滑)

    # 所有对应分类中词条频数的和
    sumCountC0 = 2.0
    sumCountC1 = 2.0

    for i in range(N):
        if trainCategory[i] == 1:
            matrixC1 = matrixC1 + trainMatrix[i]
            sumCountC1 = sumCountC1 + sum(trainMatrix[i])
        else:
            matrixC0 = matrixC0 + trainMatrix[i]
            sumCountC0 = sumCountC0 + sum(trainMatrix[i])
    #  print(sumCountC0, sumCountC1, sum(matrixC0), sum(matrixC1))
    #  sumCountC0 = sum(matrixC0)
    #  sumCountC1 = sum(matrixC1)
    #  pVectC0 = matrixC0 / sumCountC0
    #  pVectC1 = matrixC1 / sumCountC1
    pVectC0 = np.log(matrixC0 / sumCountC0) # log防止下溢
    pVectC1 = np.log(matrixC1 / sumCountC1) # log防止下溢
    return pVectC0, pVectC1, pAbusive
    
# }}}

def classifyNaiveBayes(inVect, pVectC0, pVectC1, pAbusive):# {{{
    """
    朴素贝叶斯分类函数 
    
    Parameters
    ----------
    inVect:
    
    Returns
    -------
    
    Notes
    -----
    朴素: 特征条件独立 (将所有的特征概率相乘, 就是该条信息的在对应分组的概率)
    由于存在下溢情况, 所以需要log转换一下
    ln(p1*p2*p3) = ln(p1) + ln(p2) + ln(p3)
    
    TODO: 一直无法理解pVectC0*inVect具体指的是什么意思? 暂时理解为权重吧.
    """
    #  print("p0 = ", pVectC0*inVect)
    #  print("p1 = ", pVectC1*inVect)
    p0 = np.sum(pVectC0*inVect) + np.log(1 - pAbusive)   
    p1 = np.sum(pVectC1*inVect) + np.log(pAbusive)
    #  print(p0, p1)
    if p0 > p1:
        return 0
    else:
        return 1
# }}}

def testingNB():# {{{
    dataSet, dataClass = loadDataSet()
    vocabuList = generateVocabList(dataSet)
    trainMatrix = []
    for it in dataSet:
        trainMatrix.append(setOfWord2Vec(vocabuList, it))
    pVectC0, pVectC1, pAbusive = trainingNaiveBayes(trainMatrix, dataClass)

    # 测试NB: 词集测试
    #  testEntry = ['love', 'my', 'dalmation']
    #  thisDoc = np.array(setOfWord2Vec(vocabuList, testEntry))
    #  print(classifyNaiveBayes(thisDoc, pVectC0, pVectC1, pAbusive))

    testEntry = ['stupid', 'garbage']
    thisDoc = np.array(setOfWord2Vec(vocabuList, testEntry))
    print(testEntry, classifyNaiveBayes(thisDoc, pVectC0, pVectC1, pAbusive))

    # 测试NB: 词袋测试
    #  testEntry = np.tile(['love', 'my', 'dalmation'], 5)
    #  thisDoc = np.array(setOfWord2Vec(vocabuList, testEntry))
    #  print(classifyNaiveBayes(thisDoc, pVectC0, pVectC1, pAbusive))

    testEntry = np.tile(['stupid', 'garbage'], 5)
    thisDoc = np.array(bagOfWord2Vec(vocabuList, testEntry))
    print(testEntry, classifyNaiveBayes(thisDoc, pVectC0, pVectC1, pAbusive))
# }}}

if __name__ == "__main__":
     testingNB()
