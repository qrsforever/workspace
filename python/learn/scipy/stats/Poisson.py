#!/usr/bin/python3
# -*- coding: utf-8 -*-


import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

def testPoisson():# {{{
    """
    Poisson Distribution (泊松分布)
    泊松分布的例子：已知某路口发生事故的比率是每天2次，那么在此处一天内发生n次事故的概率是多少？
    """
    # 准备数据: 已知lam:单位时间内发生某件事的平均次数
    # X轴: 单位时间内该事件发生的次数
    # Y轴: 次数对应的概率
    lam = 10  # p = 1/lam
    xs = np.arange(
            poisson.ppf(0.01, mu=lam), 
            poisson.ppf(0.99, mu=lam),
            step=1)

    # E(X) = lam, D(X) = lam
    mean, var, skew, kurt = poisson.stats(mu=lam, loc=0, moments='mvsk')
    print("mean: %.2f, var: %.2f, skew: %.2f, kurt: %.2f" % (mean, var, skew, kurt))

    fig, axs = plt.subplots(1, 3)

    # 显示pmf
    ys = poisson.pmf(xs, mu=lam)
    axs[0].plot(xs, ys, 'bo', markersize=5, label='poisson pmf')
    axs[0].legend()

    # 显示cdf
    ys = poisson.cdf(xs, mu=lam)
    axs[1].plot(xs, ys, 'bo', markersize=5, label='poisson cdf')
    axs[1].legend()

    # 随机变量RVS
    data = poisson.rvs(mu=lam, size=1000)
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
    testPoisson()
