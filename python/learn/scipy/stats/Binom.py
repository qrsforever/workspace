#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Binomial Distribution (二项分布)

import numpy as np  
from scipy import stats  
import matplotlib.pyplot as plt  

def testPmf():
    """
    为离散分布 
    二项分布的例子：抛掷10次硬币，恰好两次正面朝上的概率是多少？ 
    """

    n = 10      # 抛掷总次数
    p = 0.5     # 正面向上的概率
    k = np.arange(0, 11) # 正面朝上的次数
    binomial = stats.binom.pmf(k, n, p)
    print("sum(binomial) = ", sum(binomial)) # 概率总和为1
    print("binomial[2] = ", binomial[2])  # 正面朝上两次的概率
    plt.plot(k, binomial,'o-')  
    plt.title('Binomial: n=%i , p=%.2f' % (n, p), fontsize=15)  
    plt.xlabel('Number of successes')  
    plt.ylabel('Probability of success',fontsize=15)  
    plt.show() 

def testRvs():
    """
    为离散分布 
    使用rvs函数模拟一个二项随机变量，其中参数size指定你要进行模拟的次数。
    """

    # 返回10000个参数为n和p的二项式随机变量
    # 进行10000次实验，每次抛10次硬币，统计有几次正面朝上，
    binomsim = stats.binom.rvs(n=10, p=0.3, size=10000)  

    d = {}
    for i in binomsim:
        d[i] = d.get(i, 0) + 1

    for x, y in d.items():
        print("Count(%d) = %d" % (x, y))

    print("np.mean(binomsim) = %g" % np.mean(binomsim))
    print("np.std(binomsim) = %g" % np.std(binomsim, ddof=1)) 
  
    # 最后统计每次实验正面朝上的次数
    # x: 指定每个bin分布的数据,对应x轴
    # bins: bin的个数总共有几条条状图
    plt.hist(x=binomsim, bins=10, normed=True)  
    plt.xlabel('x')  
    plt.ylabel('density')  
    plt.show()  


if __name__ == "__main__":
    testPmf()
    testRvs()
