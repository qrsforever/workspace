#!/usr/bin/python3
# -*- coding: utf-8 -*-

# scipy模块stats文档
# http://www.cnblogs.com/ttrrpp/p/6822214.html

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def testNormal():# {{{
    """
    Normal Distribution (正态分布)
    正态分布是一种连续分布，其函数可以在实线上的任何地方取值。
    正态分布由两个参数描述：分布的平均值μ和方差σ2 。

    mu ---> loc
    sigma ---> scale

    """

    mu = 2
    sigma = 4
    xs = np.linspace(
            norm.ppf(0.01, loc=mu, scale=sigma), 
            norm.ppf(0.99, loc=mu, scale=sigma), 
            num=1000)

    # E(X) = mu, D(X) = sigma**2
    mean, var, skew, kurt = norm.stats(loc=mu, scale=sigma, moments='mvsk')
    print("mean: %.2f, var: %.2f, skew: %.2f, kurt: %.2f" % (mean, var, skew, kurt))

    fig, axs = plt.subplots(2, 2)

    # 显示pdf (norm.pdf)
    ys =norm.pdf(xs, loc=mu, scale=sigma)
    axs[0][0].plot(xs, ys, 'bo', markersize=5, label='norm.pdf')
    axs[0][0].legend()
    axs[0][0].set_title('mu = %.2f, sigma = %.2f' % (mu, sigma))

    # 显示pdf (manual)
    ys = np.exp(-((xs - mu)**2) / (2* sigma**2)) / (sigma * np.sqrt(2*np.pi))
    axs[0][1].plot(xs, ys, 'bo', markersize=5, label='cmp pdf')
    axs[0][1].legend()
    axs[0][1].set_title('mu = %.2f, sigma = %.2f' % (mu, sigma))

    # 显示cdf
    ys =norm.cdf(xs, loc=mu, scale=sigma)
    axs[1][0].plot(xs, ys, 'bo', markersize=5, label='norm.pdf')
    axs[1][0].legend()
    axs[1][0].set_title('mu = %.2f, sigma = %.2f' % (mu, sigma))

    
    # 随机变量RVS
    data = norm.rvs(loc=mu, scale=sigma, size = 1000)
    data = np.around(data, decimals=1)
    import sys
    sys.path.append("../../thinkstats")
    import Pmf
    pmf = Pmf.MakePmfFromList(data)
    xs, ys = pmf.Render()
    #  axs[1][1].plot(xs, ys, 'bo', markersize=5, label='rvs pmf')
    axs[1][1].scatter(xs, ys, label='rvs pmf')
    axs[1][1].legend()

    plt.show()
# }}}

if __name__ == "__main__":
    testNormal()
