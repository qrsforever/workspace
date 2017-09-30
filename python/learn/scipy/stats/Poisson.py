#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Poisson Distribution (泊松分布)

import numpy as np  
from scipy import stats  
import matplotlib.pyplot as plt  

def testPmf():
    """
    泊松分布的例子：已知某路口发生事故的比率是每天2次，那么在此处一天内发生n次事故的概率是多少？ 
    """
    
    # 发生事故的均值
    rate = 2
    # 该天发生0 - 10的事故的概率
    # 泊松分布的输出是一个数列，包含了发生0次、1次、2次，直到10次事故的概率。
    k = np.arange(0, 10)
    y = stats.poisson.pmf(k=k, mu=rate)

    plt.plot(k, y, 'o-')  
    plt.title('Poisson: rate=%i' % (rate), fontsize=15)  
    plt.xlabel('Number of accidents')  
    plt.ylabel('Probability of number accidents', fontsize=15)  
    plt.show()  

def testRvs():
    """
    模拟1000个服从泊松分布的随机变量 
    """

    rate = 2
    poissonsim = stats.poisson.rvs(mu=rate, loc=0, size=1000)
    
    d = {}
    for i in poissonsim:
        d[i] = d.get(i, 0) + 1

    for x, y in d.items():
        print("Count(%d) = %d" % (x, y))

    print("np.mean(poissonsim): %g" % np.mean(poissonsim))
    print("np.std(poissonsim): %g" % np.std(poissonsim, ddof=1))

    xs, ys = zip(*sorted(d.items()))

    plt.plot(xs, ys, 'o-')  
    plt.title('Poisson: rate=%i' % (rate), fontsize=15)  
    plt.xlabel('Number of accidents')  
    plt.ylabel('Probability of number accidents', fontsize=15)  
    plt.show()  


if __name__ == "__main__":
    testPmf()
    testRvs()
