#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
     模拟指数分布, 使用样本均值和样本中位数分别计算 均分误差
"""

from sample_distribution import samples
import math
import thinkstats

def CalculateMSE(sa, sb):
    return sum([(x - sb) ** 2 for x in sa]) / len(sa)

def main():
    lam = 0.5
    n = 10
    lams1 = []
    lams2 = []
    for _ in range(1000):
        data = samples('expo', n = n, lam = lam)
        s_mean = thinkstats.Mean(data)
        s_median = thinkstats.Median(data)
        lams1.append(1/s_mean)
        lams2.append(math.log(2)/s_median)

    s_lam_mean1 = thinkstats.Mean(lams1)
    s_lam_mean2 = thinkstats.Mean(lams2)
    print("Mean(lams1) = %.3f, Mean(lams2) = %.3f" % (s_lam_mean1, s_lam_mean2))

    print("MSE(lams1) = %.3f, MSE(lams2) = %.3f" % (CalculateMSE(lams1, lam), CalculateMSE(lams2, lam)))

if __name__ == "__main__":
    main()
