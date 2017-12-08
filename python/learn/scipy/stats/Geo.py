#!/usr/bin/python3
# -*- coding: utf-8 -*-

from scipy.stats import geom
import matplotlib.pyplot as plt
import numpy as np

def testGeom():# {{{
    """
    Geometric Distribution (discrete)

    Notes
    -----
        伯努利事件进行k次, 第一次成功的概率

    为什么是几何分布呢, 为什么不叫几毛分布?
    与几何数列有关 (乘积倍数)

    p: 成功的概率
    q: 失败的概率(1-p)
    k: 第一次成功时的经历的次数 (前k-1次是失败的)
        geom.pmf(k, p), (1-p)**(k-1)*p)
    """

    # 准备数据: 已知 p. 
    # X轴: 第k次才成功
    # Y轴: 概率
    p = 0.4
    xs = np.arange(geom.ppf(0.01, p), geom.ppf(0.99, p), step = 1)

    # E(X) = 1/p, D(X) = (1-p)/p**2 
    mean, var, skew, kurt = geom.stats(p, moments='mvsk')
    print("mean: %.2f, var: %.2f, skew: %.2f, kurt: %.2f" % (mean, var, skew, kurt))

    fig, axs = plt.subplots(2, 2)

    # 显示pmf1
    ys = geom.pmf(xs, p)
    axs[0][0].plot(xs, ys, 'bo', markersize=5, label='geom pmf')
    axs[0][0].vlines(xs, 0, ys, colors='b', linewidth=5, alpha=0.5, label='vline pmf')
    axs[0][0].legend(loc='best', frameon=False)

    # 显示pmf2
    ys = (1-p)**(xs-1)*p
    axs[0][1].plot(xs, ys, 'bo', markersize=5, label='geom pmf')
    axs[0][1].vlines(xs, 0, ys, colors='b', linewidth=5, alpha=0.5, label='vline pmf')
    axs[0][1].legend(loc='best', frameon=False)
    axs[0][1].set_title('ys = (1-p)**(xs-1)*p')

    # 显示cdf P(X<=x)
    ys = geom.cdf(xs, p)
    axs[1][0].plot(xs, ys, 'bo', markersize=5, label='geom cdf')
    axs[1][0].legend(loc='best', frameon=False)
    print(np.allclose(xs, geom.ppf(ys, p))) # ppf:y-->x cdf:x-->y

    # 生成随机数据(random variables)
    data = geom.rvs(p, size=1000)
    import sys
    sys.path.append("../../thinkstats")
    import Pmf
    pmf = Pmf.MakePmfFromList(data)
    xs, ys = pmf.Render()
    axs[1][1].plot(xs, ys, 'bo', markersize=5, label='rvs-pmf')

    plt.show()

# }}}


if __name__ == "__main__":
   testGeom() 
