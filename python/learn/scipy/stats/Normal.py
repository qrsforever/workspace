#!/usr/bin/python3
# -*- coding: utf-8 -*-

# scipy模块stats文档
# http://www.cnblogs.com/ttrrpp/p/6822214.html

# Normal Distribution (正态分布)

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def testPdf():
    """
    正态分布是一种连续分布，其函数可以在实线上的任何地方取值。
    正态分布由两个参数描述：分布的平均值μ和方差σ2 。
    """

    mu = 0
    sigma = 1
    xs = np.arange(-5, 5, 0.1)
    ys = stats.norm.pdf(xs, 0, 1)
    plt.plot(xs, ys)
    plt.title('Normal: $\mu$=%.1f, $\sigma^2$=%.1f' % (mu,sigma))
    plt.xlabel('x')
    plt.ylabel('Probability density', fontsize=15)
    plt.show()

if __name__ == "__main__":
    testPdf()
