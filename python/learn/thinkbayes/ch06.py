#!/usr/bin/python3
# -*- coding: utf-8 -*-

import price
import numpy
import thinkplot
import thinkbayes

def CH6_2(price1, price2):
    """
    两组展览品的价格分布
    """
    thinkplot.Clf()
    thinkplot.PrePlot(num=2)

    # 因为price变量值没有重复的, 所以PMF绘图是看不出什么的.
    # price1_pmf = thinkbayes.MakePmfFromList(price1, name='showcase1')
    # price2_pmf = thinkbayes.MakePmfFromList(price2, name='showcase2')

    price1_max = max(price1)
    price2_max = max(price2)
    price_max = max(price1_max, price2_max)
    xs = numpy.linspace(0, price_max + 100, num=150)

    price1_pdf = thinkbayes.EstimatedPdf(price1)
    price2_pdf = thinkbayes.EstimatedPdf(price2)
    price1_pmf = price1_pdf.MakePmf(xs, name='showcase1')
    price2_pmf = price2_pdf.MakePmf(xs, name='showcase2')

    thinkplot.Pmfs([price1_pmf, price2_pmf])
    thinkplot.Show(xlabel='price $', ylabel='PMF')

def CH6_5(diff1, diff2):
    """
    两组展品的出价差的CDF累计分布
    """
    thinkplot.Clf()
    thinkplot.PrePlot(num=2)

    diff1_cdf = thinkbayes.MakeCdfFromList(diff1, name='diff1')
    diff2_cdf = thinkbayes.MakeCdfFromList(diff2, name='diff2')

    thinkplot.Cdfs([diff1_cdf, diff2_cdf])
    thinkplot.Show(xlabel='diff $', ylabel="CDF")

    # 计算CDF(diff <= 0), 判断选手是否偏向低估商品
    print(diff1_cdf.Prob(0), diff2_cdf.Prob(0))
        

def main():
    """
    Showcase(正确价格游戏)

    第1组:
                       1      2      3    ...
    展品价格(price)  50969  21901  32815  ...
    选手出价(bid)    42000  14000  32000  ...
    出价差(diff)     8969   7901   815    ...

    猜测价格: 选手对每个奖品的价格猜测之和  (为什么和最后的选手出价还不一样呢)

    猜测误差 = 展品价格 - 猜测价格 ( error = price - guess )

    ?? error分布的方差和diff分布的方差相同 (不完美)

    比赛的人可以通过观看以前的比赛, 记录下自己的猜测价格和实际价格的
    猜测误差error, 从而评估自己的猜测误差的error的分布

    """
    # [(price1, price2, bid1, bid2, diff1, diff2), (), () ..]
    data2011 = price.ReadData(filename='showcases.2011.csv')
    data2012 = price.ReadData(filename='showcases.2012.csv')
    data = list(data2011) + list(data2012)
    cols = zip(*data)

    price1, price2, bid1, bid2, diff1, diff2 = cols
    #  CH6_2(price1, price2)
    print("-------------- ")
    #  CH6_5(diff1, diff2)
    print("-------------- ")

    diff1_sigma = numpy.std(diff1)
    diff2_sigma = numpy.std(diff2)
    print(numpy.mean(diff1), diff1_sigma, numpy.mean(diff2), diff2_sigma)

    # 猜测误差 高斯分布
    #  error1_pdf = thinkbayes.GaussianPdf(0, diff1_sigma)
    #  error2_pdf = thinkbayes.GaussianPdf(0, diff2_sigma)
    

if __name__ == "__main__":
    main()
    thinkplot.Clf()
