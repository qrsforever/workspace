#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import erf

def testIntelligenceScale():
    """
    通过erf.NormalCdf()得到正太分布的近似累积分布
    """

    """
    eg: 正态分布(μ=100, σ=15) 用erf.NormalCdf 函数查看正态分布中罕见事件的频数。
        高于均值, 115、130、145 的分别是多少(百分比)?
    """
    mu, sigma = 100, 15
    IQs = [mu, 115, 130, 145]
    ys = []
    for iq in IQs:
        percent = (1 - erf.NormalCdf(iq, mu=mu, sigma=sigma)) * 100
        ys.append(percent)
        print("%.2f%% people IQ > %d" % (percent, iq))

    plt.bar(IQs, ys, width=0.8, align="center")
    plt.show()


    """
    六西格玛: 超出均值6个标准差的值, 100 + 6 * 15 = 190
    """
    people = 6 * 1000 * 1000 * 1000 * (1 - erf.NormalCdf(mu + 6*sigma, mu=mu, sigma=sigma))
    print("%d people IQ > %d" % (people, 5*sigma))

    pass

if __name__ == "__main__":
    testIntelligenceScale()
