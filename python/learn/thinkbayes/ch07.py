#!/usr/bin/python3
# -*- coding: utf-8 -*-

import thinkbayes
import thinkplot
from hockey import Hockey

def CH7_1():
    """
    球队2010-2011赛季, 平均每场进球的分布, 大致为均值2.8, 标准差为0.3的高斯分布
    """
    pmf = thinkbayes.MakeGaussianPmf(2.8, 0.3, 4, n=101)
    thinkplot.Clf()
    thinkplot.Pmf(pmf)
    thinkplot.Show();

def CH7_2():
    """
    http://www.ruanyifeng.com/blog/2015/06/poisson-distribution.html
    1. 一场比赛平均进球数为lam, 每场比赛进球分布: 泊松分布
            (进球可以在任何时间点发生)
        eg. 某医院平均每小时出生3个婴儿


        重点是: 次数

    2. 进球间隔的分布: 指数分布
        eg. 某医院婴儿出生的时间间隔(20分钟一个(0.3h))

        重点是: 间隔

    泊松分布是单位时间内独立事件发生次数的概率分布 
    指数分布是独立事件的时间间隔的概率分布
    """
    # 单位时间内出生1 - 10个婴儿的泊松分布
    pmf = thinkbayes.MakePoissonPmf(3, 10, step=1)
    thinkplot.Clf()
    thinkplot.Pmf(pmf)
    #  thinkplot.Show();

    # 婴儿出生时间间隔(20分钟)
    pmf = thinkbayes.MakeExponentialPmf(0.3, 10, n=200)
    thinkplot.Clf()
    thinkplot.Pmf(pmf)
    thinkplot.Show();

def CH7_3(show = 1):
    """
    计算后验分布

    棕熊队    加人队
    bruins   canucks
      0         1
      2         3 
      8         1
      4         0
    """

    suite1 = Hockey('bruins')
    suite2 = Hockey('canucks')

    if show:
        thinkplot.Clf()
        thinkplot.PrePlot(num=2)
        thinkplot.Pmf(suite1)
        thinkplot.Pmf(suite2)
        thinkplot.Show(title='PRE', xlabel='Goals per game', ylabel='Probability')

    suite1.UpdateSet([0, 2, 8, 4])
    suite2.UpdateSet([1, 3, 1, 0])

    if show:
        # 观察最有可能lam的值, 每场比赛进球数的后验分布
        thinkplot.Clf()
        thinkplot.PrePlot(num=2)
        thinkplot.Pmf(suite1)
        thinkplot.Pmf(suite2)
        thinkplot.Show(title='POST', xlabel='Goals per game', ylabel='Probability')

    return suite1, suite2

def CH7_4(show = 1):
    """
    混合分布
    """
    suite1, suite2 = CH7_3(0)

    # 均值:
    mu1 = suite1.Mean()
    mu2 = suite2.Mean()
    print("Mean1: ", mu1)
    print("Mean2: ", mu2)


    if show:
        # 使用均值, 计算泊松分布 (下一场比赛进球分布)
        pos1 = thinkbayes.MakePoissonPmf(mu1, 10, step=1)
        pos2 = thinkbayes.MakePoissonPmf(mu2, 10, step=1)

        thinkplot.Clf()
        thinkplot.PrePlot(num=2)
        thinkplot.Pmfs([pos1, pos2])
        thinkplot.Show(title='Poisson', xlabel='Goals per game', ylabel='Probability')

    # 混合分布
    def _MixPmf(suite):
        high = 10
        metapmf = thinkbayes.Pmf()
        for lam, prob in suite.Items():
            pmf = thinkbayes.MakePoissonPmf(lam, high, step=1)
            metapmf.Set(pmf, y=prob)
        return thinkbayes.MakeMixture(metapmf, name='mix')

    mix1 = _MixPmf(suite1)
    mix2 = _MixPmf(suite2)
    
    if show:
        thinkplot.Clf()
        thinkplot.PrePlot(num=2)
        thinkplot.Pmfs([mix1, mix2])
        thinkplot.Show(title='Mixture', xlabel='Goals per game', ylabel='Probability')

    return mix1, mix2

def CH7_5():
    """
    胜算
    """
    go1, go2 = CH7_4(0)
    diff_pmf = go1 - go2

    thinkplot.Clf()
    thinkplot.Pmf(diff_pmf)
    thinkplot.Show(title='diff', xlabel='Goals per game', ylabel='Probability')

    pwin = diff_pmf.ProbGreater(0)
    pmiss = diff_pmf.ProbLess(0)
    ptie = diff_pmf.Prob(0, default=0)
    print("pwin = %.3f pmiss = %.3f ptie = %.3f" % (pwin, pmiss, ptie))


def main():
    #  CH7_1()
    #  CH7_2()
    #  CH7_3()
    #  CH7_4()
    CH7_5()
    

if __name__ == "__main__":
    main()
