#!/usr/bin/python3
# -*- coding: utf-8 -*-

import thinkbayes2
import thinkplot

class Detecter(thinkbayes2.Suite):
    """
    探测Suite
    """

    def __init__(self, r, label = 'Detecter'):
        pmf = thinkbayes2.MakePoissonPmf(r, 500, 2)
        thinkbayes2.Suite.__init__(self, pmf, r)

    def Likelihood(self, data, hypo):
        """
        似然函数 
        
        Paramters:
        ----------
        data: 计数器记录到的粒子数
        hypo: 泊松分布中每秒发射粒子个数n的假设
        
        Returns:
        --------
        
        Notes:
        -----
        
        """
        k = data
        n = hypo
        p = 0.1
        return thinkbayes2.EvalBinomialPmf(k, n, p)


def emiteParticles():
    """
    发射粒子问题
    r: 每秒发射粒子数
    n: 因为粒子(原子)有衰变, 发射到计数器上的粒子
    k: 计数器实际记录(探测)到的粒子的个数 (作为bayes的data)
    f: k的平均概率.

    
    Paramters:
    ----------
    
    Returns:
    --------
`
    Notes:
    ------
    粒子的衰变模型可以使用泊松分布(单位时间内事件发生次数的分布)
    计数器纪录粒子模型可以使用二项分布(n次独立事件, 某事件发生k次的概率)

    正向思维:
        泊松分布: thinkbayes2.MakePoissonPmf()
        二项分布: thinkbayes2.MakeBinomialPmf()

    逆向思维:
        
    """

    # _test1, _test2 是正向思维, 即知道系统模型的参数, 求数据(的分布)
    def _test1(show = 0):
        # 已知r, 求n的分布 即泊松分布
        r = 150
        # MakePoissonPmf: 存在一个上限(无极限), 需要归一化
        pmf = thinkbayes2.MakePoissonPmf(r, 2*r, 1)
        if show:
            thinkplot.Clf()
            thinkplot.Pmf(pmf)
            thinkplot.Show(title="test1", xlabel='Event Count', ylabel='Probality')
        print("Total: ", pmf.Total())
        return pmf

    def _test2(show):
        # 已知n, f(纪录到的概率), 求k的分布, hypo
        n = 150
        f = 0.1
        # MakeBinomialPmf: 二项分布 0 - n次已经罗列了所有可能, 不需要归一化
        pmf = thinkbayes2.MakeBinomialPmf(n, f)
        if show:
            thinkplot.Clf()
            thinkplot.Pmf(pmf)
            thinkplot.Show(title="test2", xlabel='Event Count', ylabel='Probality')
        print("Total: ", pmf.Total())
        return pmf

    # n的分布测试
    #  _test1(0)
    # n的分布作为(假设)已知, 求k(粒子计数器纪录到的粒子个数)的分布
    #  _test2(0)
    
    # Bayes 是逆向思维, 知道数据的提前下, 求模型参数(的概率)
    # 已知r(平局每秒发射的粒子个数), 初始化一个泊松分布
    thinkplot.Clf()
    thinkplot.PrePlot(num=3)
    for r in [100, 250, 400]:
        suite = Detecter(r)
        suite.Update(15)
        thinkplot.Pmf(suite)
        print("MaxLikelihoood: ", suite.MaximumLikelihood())

    thinkplot.Show(title='Detecter', xlabel='hypo', ylabel='Probality')


def main():
    emiteParticles()

if __name__ == "__main__":
    main()
