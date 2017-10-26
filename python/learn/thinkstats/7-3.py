#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
在 NSFG 的数据中,第一胎婴儿体重的分布与非第一胎婴儿体重的分
布不同的后验概率是多少?

贝叶斯统计解释(HA是与H0相对的假设):
P(Ha|E) = P(E|Ha)P(Ha) / P(E):
P(E) = P(E|Ha)P(Ha) + P(E|H0)P(H0)

P(Ha) : 观察到这效应之前的先验概率
P(E|Ha) : 在Ha条件成立的情况下, 观测到效应E的概率
P(E): 在任意情况下观察到效应E的概率

P-Value = P(E|H0): 在原假设条件下, 出现直观效应的概率

if P(Ha) = 0.5 then P(H0) = 1 - 0.5 = 0.5
P(E|Ha) = ?
P(Ha|E) = ?

P(H0) Sample P-Value:
    将A, B分组数据混合, 再分别抽取Na, Nb个数据计算平均值差分布

P(Ha) Sample P-Value:
    分别在A组抽取Na个数据, B组抽取Nb个数据, 计算平均值差分布

"""

import hypothesis
import Babies
import thinkstats

p = 0

def main():
    firsts, others, babies = Babies.PartitionBabies()
    if p == 0:
        firsts_wtlist = Babies.GetWightList(firsts)
        others_wtlist = Babies.GetWightList(others)
        babies_wtlist = Babies.GetWightList(babies)
    else:
        firsts_wtlist = Babies.GetPregnacyList(firsts)
        others_wtlist = Babies.GetPregnacyList(others)
        babies_wtlist = Babies.GetPregnacyList(babies)

    print('(Mean, Var) of babies data', thinkstats.MeanVar(babies_wtlist))

    # P(E|H0)
    peh0 = hypothesis.Test("peh0", firsts_wtlist, others_wtlist, babies_wtlist, babies_wtlist, iters=1000, plot=False)

    # P(E|Ha)
    peha = hypothesis.Test("peh0", firsts_wtlist, others_wtlist, firsts_wtlist, others_wtlist, iters=1000, plot=False)

    # P(HA)
    pha = 0.5

    # P(E)
    pe = peha * pha + peh0 * (1 - pha)

    # P(Ha|E)
    phae = (peha * pha) / pe
    print("pha = %.3f, peh0 = %.3f, peha = %.3f, phae = %.3f" % (pha, peh0, peha, phae))

if __name__ == "__main__":
    main()
