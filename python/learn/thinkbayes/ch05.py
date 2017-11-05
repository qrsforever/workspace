#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
贝叶斯统计的基本操作是update, 这需要先验概率和一组数据, 并产生一个后验概率分布.

其他操作:
    缩放, 加法, 最大值, 最小值等
"""

import thinkbayes
import thinkplot

class Die(thinkbayes.Pmf):
    """
    一个骰子
    """
    def __init__(self, sides = 6):
        """
        sides: 面数
        """
        thinkbayes.Pmf.__init__(self)
        for x in range(1, sides+1):
            self.Set(x, y=1)
        self.Normalize(fraction=1.0)

def CH5_4():
    """
    加法操作:

    转动3个6面的骰子, 计算它们的和, 采用下面两种方式, 对比分布图.

    模拟:
        通过模拟随机样品, 累积和.
    枚举:
        枚举所有可能的数字对
    """

    d6 = Die(6)
    k = 3
    print("mean(d6) = %.3f, sum(probs) = %.3f" % (d6.Mean(), d6.Total()))

    # 模拟: 3个骰子分布, N越大越精确. 缺点: 耗时.
    N = 1000
    dists = [d6] * k
    pmf = thinkbayes.SampleSum(dists, N)
    pmf.name = 'sim'
    thinkplot.Pmf(pmf)
    print("mean([d6]*3) = %.3f, sum(*) = %.3f" % (pmf.Mean(), pmf.Total()))

    # 枚举: x数值相加, y概率相乘
    pmf = d6 + d6 + d6
    pmf.name = 'enum'
    thinkplot.Pmf(pmf)
    thinkplot.Show(xlabel='sum([d6]*3)', ylabel='probablity')
    print("mean([d6]*3) = %.3f, sum(*) = %.3f" % (pmf.Mean(), pmf.Total()))

def RandomMax(dists):
    return max(dist.Random() for dist in dists)

def SampleMax(dists, n):
    return thinkbayes.MakePmfFromList([RandomMax(dists) for x in range(n)])

def PmfMax(pmf1, pmf2):
    res = thinkbayes.Pmf()
    for v1, p1 in pmf1.Items():
        for v2, p2 in pmf2.Items():
            res.Incr(max(v1, v2), p1*p2)
    return res

def CH5_5():
    """
    最大值操作:
    转动3个6面的骰子, 计算它们的最大值 采用下面三种方式, 对比分布图.
    
    模拟:
    枚举:
    指数计算:

    """

    d6 = Die(6)
    k = 3
    
    # 模拟
    N = 1000
    dists = [d6] * k
    pmf = SampleMax(dists, N)
    pmf.name = 'sim'
    thinkplot.Pmf(pmf)

    # 枚举 km^2
    pmf = PmfMax(d6, d6) 
    print("pmf1.Total() = %.3f" % pmf.Total())
    pmf = PmfMax(pmf, d6)
    print("pmf2.Total() = %.3f" % pmf.Total())
    pmf.name = 'enum'
    thinkplot.Pmf(pmf)

    # CDF (指数max) TODO 不是很明白???
    cdf = d6.Max(k)
    cdf.name = "expo"
    thinkplot.Cdf(cdf)

    thinkplot.Show(xlabel='max([d6]*3)', ylabel='probablity')

def CH5_6():
    """
    混合分布, 汇总多个分布的贡献

    骰子个数    骰子面数
      5          4-sides
      4          6-sides
      3          8-sides
      2         12-sides
      1         20-sides
    """
    thinkplot.PrePlot(num=2)

    # (权重, 骰子)
    dices=[ (5, Die(4)), 
            (4, Die(6)), 
            (3, Die(8)), 
            (2, Die(12)), 
            (1, Die(20))]
    mix = thinkbayes.Pmf() 
    for w, die in dices:
        for v, p in die.Items():
            mix.Incr(v, w*p)
    mix.Normalize()
    mix.name = 'mix-1'
    thinkplot.Pmf(mix)

    # 方法2
    pmf_dices = thinkbayes.Pmf()
    pmf_dices.Set(Die(4), y=5)
    pmf_dices.Set(Die(6), y=4)
    pmf_dices.Set(Die(8), y=3)
    pmf_dices.Set(Die(12), y=2)
    pmf_dices.Set(Die(20), y=1)
    pmf_dices.Normalize()
    mix = thinkbayes.MakeMixture(pmf_dices, name='mix-2')
    mix.name = 'mix-2'
    thinkplot.Pmf(mix)

    thinkplot.Show()

def main():
    CH5_4()
    print("-------------- ")
    CH5_5()
    print("-------------- ")
    CH5_6()

if __name__ == "__main__":
    main()
