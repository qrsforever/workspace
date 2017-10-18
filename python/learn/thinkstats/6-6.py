#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
从 BRFSS(见 4.5 节)的数据中,我们发现人类身高大致服从正态分
布,男性身高的均值为 178 cm、方差为 59.4 cm;女性身高的均值为
163 cm、方差为 52.8 cm。
蓝人乐团要求成员为男性,身高介于 178 cm 和 185 cm 之间,那么在
美国男性中身高介于该区间的人有多少?
"""

import math
import brfss
import Cdf
import myplot

def main():
    resp = brfss.Respondents()
    resp.ReadRecords(data_dir='res')
    d = resp.SummarizeHeight()
    man_l = d[1]
    cdf = Cdf.MakeCdfFromList(man_l, name='man height')
    mu = cdf.Mean()
    var = cdf.Var(mu=mu)
    sigma = math.sqrt(var)
    print("man height: mean = %.3f var = %.3f sigma = %.3f" %
            (mu, var, sigma))
    myplot.Cdf(cdf, complement=False, transform=None)
    myplot.Show()
    v = (cdf.Prob(185) - cdf.Prob(178))*100
    print("178 - 185: %.3f%%" % v)

if __name__ == "__main__":
    main()
