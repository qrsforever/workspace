#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy

"""
编写一个函数,从一个均值为 0、方差为 1 的正态分布中产生 6 个随
机数,利用这些随机数估计均值,并计算误差 x-μ。运行 1000 次这
个函数,计算均方误差。

MSE : Mean Squared Error
"""

def CalculateMSE(xs_, mu):
    """
    计算均方误差
    xs_: 所有样本均值
    mu: 总体均值
    """
    return sum([(x - mu) ** 2 for x in xs_]) / len(xs_)

def main():
    #  numpy.random.seed(seed=1)
    mu = 0
    sigma = 1
    size = 6
    items = 10
    xs1_ = []
    xs2_ = []
    for _ in range(items) :
        s = numpy.random.normal(loc=mu, scale=sigma, size=size)
        xs1_.append(sum(s)/size)
        i = int(size / 2)
        if size % 2:
            xs2_.append((s[i-1] + s[i])/2)
        else:
            xs2_.append(s[i]/2)
    mse1 = CalculateMSE(xs1_, mu)
    print("mse1 = ", mse1)

    mse2 = CalculateMSE(xs2_, mu)
    print("mse2 = ", mse2)

if __name__ == "__main__":
    main()
