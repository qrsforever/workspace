#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
random 模块中的 expovariate 函数可以为给定 λ 生成服从指数分布
的随机数。用这个函数生成 44 个服从随机分布且均值为 32.6 的数
"""

import math, random
import myplot
import Cdf

def main():
    # 通过公式计算F(X)
    lamb = 1/32.6
    xs = sorted([random.expovariate(lamb) for i in range(43)])
    ys = [1-pow(math.e, -lamb*x) for x in xs]
    myplot.Plot(xs, ys, label='formular')

    # 通过累计统计F(X) ---> 经验CDF
    cdf = Cdf.MakeCdfFromList(xs, name='expovariate')
    myplot.Cdf(cdf, complement=False, transform=None)
    myplot.Show()


if __name__ == "__main__":
    main()
