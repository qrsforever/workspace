#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Exponential Distribution (指数分布)

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def testPdf():
    """
    连续概率分布，用于表示独立随机事件发生的时间间隔。
    比如旅客进入机场的时间间隔、打进客服中心电话的时间间隔、中文维基百科新条目出现的时间间隔等等。
    """

    lambd = 0.5 # 均值mu = 1 / 0.5 = 2
    xs = np.arange(0, 15, 0.1)
    #  ys = stats.expon.pdf(xs)
    ys =lambd * np.exp(-lambd * xs)
    plt.plot(xs, ys)
    plt.title('Exponential: $\lambda$=%.2f' % (lambd))
    plt.xlabel('x')
    plt.ylabel('Probability density', fontsize=15)
    plt.show()
    pass

def testRvs():
    """
    模拟1000个随机变量。scale参数表示λ的倒数。函数np.std中，参数ddof等于标准偏差除以n-1的值。
    """

    lambd = 0.5
    exponsim = stats.expon.rvs(scale=1/lambd, size=1000)
    print("np.mean(exponsim): %g" % np.mean(exponsim))
    print("np.std(exponsim): %g" % np.std(exponsim, ddof=1))

    plt.hist(exponsim, bins=20, normed=True)
    plt.xlim(0, 15)
    plt.title('Simulating Exponential Random Variables')
    plt.show()


if __name__ == "__main__":
    testPdf()
    testRvs()
