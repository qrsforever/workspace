#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
编写一个函数,从一个均值为 0、方差为 1 的正态分布中产生 6 个随
机数,利用样本方差去估计 σ**2 ,并计算估计误差 S**2 - σ**2 。运行这个函数
1000 次,计算平均的误差(这里没有对误差进行平方)。
"""

import numpy

def main():
    numpy.random.seed(seed=0)    
    mu = 0
    sigma = 1
    errs = []
    for _ in range(1000):
        sample = numpy.random.normal(loc=mu, scale=sigma, size=100)
        s_var = numpy.var(sample)
        errs.append(s_var - sigma**2)
    print("Mean(errs) = ", numpy.mean(errs))

if __name__ == "__main__":
    main()
