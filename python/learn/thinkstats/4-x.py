#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import Babies
import Pmf
import Cdf
import myplot
import erf

def CmpNormalModelWithDataSample():
    firsts, others, babies = Babies.PartitionBabies() 
    weights = Babies.GetWightList(babies)
    pmf = Pmf.MakePmfFromList(weights)
    mu = pmf.Mean()
    var = pmf.Var(mu)
    sigma = math.sqrt(var)
    print("mu = {}, var = {}, sigma = {}".format(mu, var, sigma))

    # 经验分布, 数据
    cdf = Cdf.MakeCdfFromPmf(pmf, name='data')
    myplot.cdf(cdf)

    # u, sigma --> 误差函数计算 模型
    xs, yy = pmf.Render()
    ys = [erf.NormalCdf(x, mu, sigma) for x in xs]
    myplot.Plot(xs, ys, label='Model')
    myplot.Show()
    myplot.Clf()

def main():
    CmpNormalModelWithDataSample()

if __name__ == "__main__":
    main()
