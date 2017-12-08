#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt

def testExpon():# {{{
    """
    Exponential Distribution (指数分布[又叫负指数分布]: continuous)

    连续概率分布,用于表示独立随机事件发生的时间间隔。
    比如旅客进入机场的时间间隔,打进客服中心电话的时间间隔,中文维基百科新条目出现的时间间隔等等.

    lambda: rate parameter
            pdf = lambda * exp(-lambda * x)
    E(X) = 1/lambda (如果你平均每个小时接到2次电话，那么你预期等待每一次电话的时间是半个小时.)
    """

    # 准备数据: 已知lam, 某件事件单位事件发生的次数(频率)
    # X轴: 间隔时间
    # Y轴: 某时间点上的密度(可以大于1)
    lam = 0.5
    theta = 1/lam
    xs = np.linspace(expon.ppf(0.01, scale=theta), expon.ppf(0.99, scale=theta), num=1000)

    # E(X) = 1/lam 即　(theta), D(X) = 1/(lam**2) 即 (theta**2)
    mean, var, skew, kurt = expon.stats(loc=0, scale=theta, moments='mvsk')
    print("mean: %.2f, var: %.2f, skew: %.2f, kurt: %.2f" % (mean, var, skew, kurt))

    fig, axs = plt.subplots(2, 2)
    #  fig.set_figheight(10)
    #  fig.set_figwidth(14)
    #  print(fig.get_dpi(), fig.get_figheight(), fig.get_figwidth())

    # 显示pdf (使用expon.pdf)
    ys = expon.pdf(xs, scale=theta)
    axs[0][0].plot(xs, ys, 'bo', markersize=5, label='expon pdf')
    axs[0][0].legend()
    axs[0][0].set_title('lambda = %.2f' % lam)
    axs[0][0].set_xlabel(u"间隔时间")
    axs[0][0].set_ylabel(u"概率密度")

    # 显示pdf (使用np.exp)
    ys = lam * np.exp(-lam * xs)
    axs[0][1].plot(xs, ys, 'bo', markersize=5, label='np exp')
    axs[0][1].legend()
    axs[0][1].set_title('lambda = %.2f' % lam)

    # 显示cdf
    ys = expon.cdf(xs, scale=theta)
    axs[1][0].plot(xs, ys, 'bo', markersize=5, label='expon cdf')
    axs[1][0].legend()
    axs[1][0].set_title('lambda = %.2f' % lam)

    # 随机变量RVS
    data = expon.rvs(scale=theta, size = 1000)
    data = np.around(data, decimals=1)
    import sys
    sys.path.append("../../thinkstats")
    import Pmf
    pmf = Pmf.MakePmfFromList(data)
    xs, ys = pmf.Render()
    #  axs[1][1].plot(xs, ys, 'bo', markersize=5, label='rvs pmf')
    axs[1][1].scatter(xs, ys, label='rvs pmf')
    axs[1][1].legend()
    axs[1][1].set_xlabel(u"间隔时间")
    axs[1][1].set_ylabel(u"量化后的概率")

    plt.show()
# }}}

if __name__ == "__main__":
    testExpon()
