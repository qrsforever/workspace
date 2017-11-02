#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
"""

from thinkbayes import Suite, Pmf
import thinkbayes
import thinkplot

"""
数字作为假设
"""

class Dice(Suite):
    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0/hypo

def CH3_1():
    """
    Dice(骰子)问题
    骰子按几个面分为: 4, 6, 8, 12, 20种骰子
    随机选择一个骰子, 摇出了数字6, 问选择骰子的概率

    D: 假设使用这个骰子摇出了数字6

             p(H)      p(D/H)     p(H)p(D/H)     p(H/D)
    假设   先验概率    似然度       Mult        后验概率
     4       1/5         0           0        |    0    |
     6       1/5        1/6         1/30      |  0.392  |
     8       1/5        1/8         1/40      |  0.294  |
     12      1/5        1/12        1/60      |  0.196  |
     20      1/5        1/20        1/100     |  0.118  |
                                              +---------+
    ---> 继续用这个骰子摇出数字8                   |
                                                   |
               +-----------------------------------+
               | 后验概率变为先验概率
               |
               v
              p(H)      p(D/H)     p(H)p(D/H)     p(H/D)   
     假设   先验概率    似然度       Mult        后验概率  
      4        0          0           0              0     
      6      0.392        0           0              0      
      8      0.294       1/8          -              -          
      12     0.196       1/12         -              -            
      20     0.118       1/20         -              -             

    """

    # 摇出6
    hypoes = [4, 6, 8, 12, 20]
    data = 6
    suite = Dice(hypoes)
    suite.Update(data)
    suite.Print()

    # 继续摇出[6,8,7,7,5,4], 顺序不敏感
    dataset = [6, 8, 7, 7, 5, 4]
    for data in dataset:
        print("-------------- ")
        suite.Update(data)
        suite.Print()

class Train(Dice):
    """
    火车头Suite
    先验概率为均匀分布
    """

def CH3_2():
    """
    火车头问题(Train)
    有一天看到一个编号60的火车头经过, 论共有多少个火车头?
    假设 上限 N = 1000, 500, 2000
    猜测结果对上限敏感

    实际N个火车头, 假设看到了60号火车头
    
    1       1/N      0
    2       1/N      0
    ...     ...     ...
    59      1/N      0
    60      1/N     1/60
    61      1/N     1/61
    ...     ...     ...
    1000    1/N     1/1000
    """

    # 假设有1 - 1000个编号的火车头
    N = 1000
    hypoes = range(1, N)
    suite = Train(hypoes) 
    suite.Update(60)
    thinkplot.PrePlot(num=1)
    thinkplot.Pmf(suite)
    thinkplot.Show(title='Train', xlabel='Number of trains', ylabel='Probability')
    print(suite.Mean())

def CH3_3():
    """
    两种方法使 后验均值分布收敛:
    <1> 获取更多的数据   (v)
    <2> 更多的背景信息
    """
    # N: 上限
    for N in [500, 1000, 2000]:
        hypoes = range(1, N)
        suite = Train(hypoes)
        # 获取更多的数据
        for data in [60, 30, 90]:
            suite.Update(data)
        print("Upper= %4d\t\t Mean(p(H/D)) = %4.0f" % (N, suite.Mean()))

class Train2(Dice):
    """
    先验概率为指数分布
                   alpha
    PMF(x) ~ [(1/x)]    
    """

    def __init__(self, hypoes, alpha=1.0):
        Pmf.__init__(self)
        for hypo in hypoes:
            self.Set(hypo, hypo ** (-alpha))
        self.Normalize(fraction=1.0)

def CH3_4():
    """
    不同先验计算后验
    Train: 先验概率为 均匀分布uniform
    Train2: 先验概率为 指数分布power law

    alpha = 1:
    +-------------------------------------+
    |    先验概率(未归一化)               |
    | 1       1/1              0          |
    | 2       1/2              0          |
    | ...     ...             ...         |
    | 59      1/59             0          |
    | 60      1/60            1/60        |
    | 61      1/61            1/61        |
    | ...     ...                         |
    | 1000    1/1000          1/1000      |  
    +-------------------------------------+
    """
    dataset = [60]
    N = 1000

    def _makePosterior(uppernum, constructor, dataset):
        """
        根据构造器函数和数据集, 生成后验概率suite
        """
        suite = constructor(range(1, uppernum))
        for data in dataset:
            suite.Update(data)
        return suite

    thinkplot.Clf()
    thinkplot.PrePlot(num=2)
    constructors = [Train, Train2]
    labels = ['uniform', 'power law']

    for constructor, label in zip(constructors, labels):
        suite = _makePosterior(N, constructor, dataset)
        suite.name = label
        thinkplot.Pmf(suite)

    thinkplot.Show(title='compare priors', xlabel='Number of trains', ylabel='prob')

    dataset = [60, 30, 90]
    for constructor, label in zip(constructors, labels):
        for n in [500, 1000, 2000]:
            suite = _makePosterior(n, constructor, dataset)
            # 单点估计
            print("%s: n = %d, mu = %.3f" % (label, n, suite.Mean()))
            # 后验概率的置信区间5% - 95% (see CH3_5)
            interval = thinkbayes.Percentile(suite, 5), thinkbayes.Percentile(suite, 95)
            print(interval)

            # CH3_6, 累计分布函数计算百分位数
            if n == 2000:
                cdf = thinkbayes.MakeCdfFromPmf(suite)
                interval = cdf.Percentile(5), cdf.Percentile(95)
                print("MakeCdfFromPmf:", interval)
            

def main():
    #  CH3_1()
    #  print("-------------- ")
    #  CH3_2()
    #  print("-------------- ")
    #  CH3_3()
    #  print("-------------- ")
    CH3_4()
    print("-------------- ")

if __name__ == "__main__":
    main()
