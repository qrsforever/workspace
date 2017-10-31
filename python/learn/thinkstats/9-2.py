#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
请编写一个计算相关系数的函数 Corr ,该函数可接受两组数据。提
示:这里可以用到之前的函数 thinkstats.Var 和 Cov 。
"""

import brfss
import thinkstats
import correlation
import math

def Corr(xs, ys):
    """
    计算皮尔逊相关系数 (协方差--->标准分数)
    皮尔逊相关系数对异常值的影响很敏感
    """
    cov = correlation.Cov(xs, ys)
    _, xs_var = thinkstats.MeanVar(xs)
    _, ys_var = thinkstats.MeanVar(ys)
    return cov / (math.sqrt(xs_var * ys_var))

def main():
    resp = brfss.Respondents()
    resp.ReadRecords(data_dir='res')
    heights, weights = resp.GetHeightAndWeight()

    r1 = Corr(heights, weights)
    # 方法2
    r2 = correlation.Corr(heights, weights)
    print(r1, "vs",  r2)

    print("E = 1 vs", Corr(heights, heights))

if __name__ == "__main__":
    main()
