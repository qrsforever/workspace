#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import random
import thinkstats
import Pmf
import Cdf
import erf
import myplot

def normal_sample(n, mu, sigma):
    return [random.normalvariate(mu, sigma) for i in range(n)]

def process(data):
    # Hist 分布图
    hist = Pmf.MakeHistFromList(data, name='hist') 
    myplot.Hist(hist, color='blue')
    myplot.Show()

    # Pmf 分布图
    pmf = Pmf.MakePmfFromHist(hist, name='pmf')
    myplot.Pmf(pmf, color='yellow')
    myplot.Show()
    
    myplot.Clf()

    # 实际数据的CDF分布图
    cdf = Cdf.MakeCdfFromList(data, name='loafs')
    myplot.Cdf(cdf)

    mu, var = thinkstats.MeanVar(data) 
    sigma = math.sqrt(var)
    print("mu = %.3f, sigma = %.3f" % (mu, sigma)) 

    # 正态分布
    xs = normal_sample(len(data), mu, sigma) # xs = data
    ys = [erf.NormalCdf(x, mu=mu, sigma=sigma) for x in xs]
    myplot.Scatter(xs, ys, color='red',label='sample')
    myplot.Show()

def main():
    for n in range(1, 20):
        m = []
        # 一年中, 每天从样本n中选择最大的, 组成新的样本m
        for d in range(365):
            l = normal_sample(n, 950, 50)
            m.append(int(max(l)))

        # 计算样本m的mu, sigma
        mu = thinkstats.Mean(m) 

        # 如果mu大于1000, 停止试验, 画图cdf
        if mu >= 1000:
            process(m)
            break;

if __name__ == "__main__":
    main()
