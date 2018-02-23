#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

def testBinom():# {{{
    """
    Binomial Distribution (二项分布 discrete)

    二项分布的例子：抛掷10次硬币，恰好两次正面朝上的概率是多少？

    事件要么发生, 要么不发生

    """

    # 准备数据: 已知 n(伯努利实验次数), p(某件事件发生的概率)
    # X轴: n次实验中事件出现k次
    # Y轴: 概率
    n = 100 # 当n很大(np > 5 && nq > 5) 近似 X ~ N(np, npq)
    p = 0.5
    xs = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))

    # E(X) = np, D(X) = np(1-p)
    mean, var, skew, kurt = binom.stats(n, p, loc=0, moments='mvsk')
    print("mean: %.2f, var: %.2f, skew: %.2f, kurt: %.2f" % (mean, var, skew, kurt))

    fig, axs = plt.subplots(1, 3)

    # 显示pmf
    ys = binom.pmf(xs, n, p)
    axs[0].plot(xs, ys, 'bo', markersize=5, label='binom pmf')
    axs[0].legend()

    # 显示cdf
    ys = binom.cdf(xs, n, p)
    axs[1].plot(xs, ys, 'bo', markersize=5, label='binom cdf')
    axs[1].legend()

    # 随机变量RVS
    data = binom.rvs(n, p, size=1000)
    import sys
    sys.path.append("../../thinkstats")
    import Pmf
    pmf = Pmf.MakePmfFromList(data)
    xs, ys = pmf.Render()
    axs[2].plot(xs, ys, 'bo', markersize=5, label='rvs pmf')
    axs[2].legend()

    plt.show()

# }}}

if __name__ == "__main__":
    testBinom()
