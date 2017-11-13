#!/usr/bin/python3
# -*- coding: utf-8 -*-

import thinkbayes
import thinkplot

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

    2. 进球间隔的分布: 指数分布
        eg. 某医院婴儿出生的时间间隔(20分钟一个(0.3h))

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

def main():
    #  CH7_1()
    print("-------------- ")
    CH7_2()


if __name__ == "__main__":
    main()
