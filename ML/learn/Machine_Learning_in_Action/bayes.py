#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import re
import random

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

def setOfWords2Vec(vocabuList, documents):# {{{
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

def bagOfWords2Vec(vocabuList, documents):# {{{
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

    问题出发:
        给一个评论,计算属于哪个分类的概率, 不好直接实现, 
        如果某个分类下出现这个条评论的概率可以计算
        使用NB

    1. 已知先验概率, 在测试集中, 好/坏评论分类的概率
    2. 训练集, 计算出每个分类中特征词条的概率 ---> 条件概率(这里是iid,独立同)
    3. 测试集, 算出每个分类出现该评断的概率, 最大的概率就是分析的结果 (最大似然)


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
        trainMatrix.append(setOfWords2Vec(vocabuList, it))
    pVectC0, pVectC1, pAbusive = trainingNaiveBayes(trainMatrix, dataClass)

    # 测试NB: 词集测试
    #  testEntry = ['love', 'my', 'dalmation']
    #  thisDoc = np.array(setOfWords2Vec(vocabuList, testEntry))
    #  print(classifyNaiveBayes(thisDoc, pVectC0, pVectC1, pAbusive))

    testEntry = ['stupid', 'garbage']
    thisDoc = np.array(setOfWords2Vec(vocabuList, testEntry))
    print(testEntry, classifyNaiveBayes(thisDoc, pVectC0, pVectC1, pAbusive))

    # 测试NB: 词袋测试
    #  testEntry = np.tile(['love', 'my', 'dalmation'], 5)
    #  thisDoc = np.array(setOfWords2Vec(vocabuList, testEntry))
    #  print(classifyNaiveBayes(thisDoc, pVectC0, pVectC1, pAbusive))

    testEntry = np.tile(['stupid', 'garbage'], 5)
    thisDoc = np.array(bagOfWords2Vec(vocabuList, testEntry))
    print(testEntry, classifyNaiveBayes(thisDoc, pVectC0, pVectC1, pAbusive))
# }}}

def parseWordsFromText(text):# {{{
    """
    从文档数据中解析出单词

    忽略小于3个字符的单词, 字符统一转变为小写
    """

    wordsList = re.split(r'\W*', text)
    return [word.lower() for word in wordsList if len(word) > 2]

# }}}

def testSpamMail():# {{{
    """
    过滤垃圾邮件 

    Notes
    -----
    """
    emailRootDir = "machinelearninginaction/Ch04/email"
    emailHamDir = os.path.join(emailRootDir, "ham")
    emailSpamDir = os.path.join(emailRootDir, "spam")
    
    dataSet = []
    classesList = []
    for i in range(1, 26):
        wordsList = parseWordsFromText(open("%s/%i.txt" % (emailHamDir, i), encoding="ISO-8859-1").read())
        dataSet.append(wordsList)
        classesList.append(0)  # 正常邮件
        wordsList = parseWordsFromText(open("%s/%i.txt" % (emailSpamDir, i), encoding="ISO-8859-1").read())
        dataSet.append(wordsList)
        classesList.append(1)  # 垃圾邮件

    # 去重, 生成一个词汇集合List, 可以删除一些常用单词
    vocabuList =  generateVocabList(dataSet)

    # 将dataSet集合中的数据转换为词汇向量形式
    #  dataMatrix = []
    #  for doc in dataSet:
        #  dataMatrix.append(bagOfWords2Vec(vocabuList, doc))
    #  N = len(dataMatrix)

    # 将dataSet分为训练集和测试集(10)
    trainingIndexSet = [i for i in range(50)]
    testIndexSet = []; testClasses = []
    for i in range(10):
        idx = int(random.uniform(0, len(trainingIndexSet)))
        testIndexSet.append(idx)
        del(trainingIndexSet[idx])

    # 训练集
    trainingMatrix = []; trainingClasses = []
    for idx in trainingIndexSet:
        trainingMatrix.append(bagOfWords2Vec(vocabuList, dataSet[idx]))
        trainingClasses.append(classesList[idx])

    # 测试集
    testMatrix = []; testClasses = []
    for idx in testIndexSet:
        testMatrix.append(bagOfWords2Vec(vocabuList, dataSet[idx]))
        testClasses.append(classesList[idx])
    
    # 分别计算出 垃圾(1)/正常(0) 两类邮件词汇使用的频率向量
    # pSpam: 垃圾邮件的先验概率
    p0, p1, pSpam = trainingNaiveBayes(trainingMatrix, trainingClasses)

    # 测试
    errCount = 0
    for i in range(len(testMatrix)):
        isSpam = classifyNaiveBayes(testMatrix[i], p0, p1, pSpam)
        if isSpam != testClasses[i]:
            errCount += 1
    print("errCount = %d, errRate = %.2f%%" % (errCount, errCount*100/len(testMatrix)))

# }}}

if __name__ == "__main__":
     testingNB()
     testSpamMail()
