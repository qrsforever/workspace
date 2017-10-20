#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
在 NSFG 的数据集中,第一胎婴儿的平均体重与非第一胎婴儿的平均
体重的差异为 2.0 盎司。请计算这个差异的 p 值。
"""

import Babies
import thinkstats
import time
import random
import Cdf
import myplot


def DifferenceInMean(alist, blist):
    """
    计算两组数据的平均值的差
    """
    firsts_mu = thinkstats.Mean(alist)
    others_mu = thinkstats.Mean(blist)
    delta = firsts_mu - others_mu
    return firsts_mu, others_mu, delta

def GeneratorDeltas(t, n, m):
    """
    产生两组样本计算平均值之差
    """
    sample1 = SamplesWithReplacement(t, n)
    sample2 = SamplesWithReplacement(t, m)
    mu1, mu2, delta = DifferenceInMean(sample1, sample2)
    return delta

def SamplesWithReplacement(t, n):
    """
    有放回抽样
    """
    sample = [ random.choice(t) for i in range(n) ]
    return sample

show = 1
def main():
    random.seed(time.clock()) 
    firsts, others, babies = Babies.PartitionBabies()
    n = len(firsts)
    m = len(others)
    s = len(babies)
    print("n = %d, m = %d, s = %d" % (n, m, s))

    firsts_wtlist = Babies.GetWightList(firsts)
    others_wtlist = Babies.GetWightList(others)
    babies_wtlist = Babies.GetWightList(babies)
    print('(Mean, Var) of babies data', thinkstats.MeanVar(babies_wtlist))
    #  babies_wtlist.extend(firsts_wtlist)
    #  babies_wtlist.extend(others_wtlist)
    firsts_mu, others_mu, delta = DifferenceInMean(firsts_wtlist, others_wtlist)
    delta = abs(delta)
    print("Actual: firsts_mu = %.2f others_mu = %.2f delta = %.2f" % (firsts_mu, others_mu, delta))

    deltas = [ GeneratorDeltas(babies_wtlist, n, m) for i in range(1000) ]

    mu, var = thinkstats.MeanVar(deltas)
    print("Samples: deltas_mu = %.2f, deltas_var = %.2f" % (mu, var))
    cdf = Cdf.MakeCdfFromList(deltas, name='diff mu list')

    # P-Value
    pleft = cdf.Prob(-delta)
    pright = 1.0 - cdf.Prob(delta)
    pvalue = pleft + pright
    print("pleft = %.2f, pright = %.2f, pvalue = %.2f" % (pleft, pright, pvalue))

    # plot
    if show:
        myplot.Cdf(cdf, complement=False, transform=None)
        myplot.Show()

if __name__ == "__main__":
    main()
