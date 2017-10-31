#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
请编写一个计算两个数据序列协方差的函数 Cov ,为了测试你写的函
数,可以计算两个相同序列的协方差,确保有 Cov(X, X)=Var(X)。
"""

import brfss
import thinkstats
import correlation

def Cov(xs, ys):
    """
    协方差, 算出来的值很难看, 单位也没意义.
    """
    xn = len(xs)
    yn = len(ys)
    if xn != yn:
        return 0
    x_mu = thinkstats.Mean(xs)
    y_mu = thinkstats.Mean(ys)
    t = [(x-x_mu)*(y-y_mu) for x, y in zip(xs, ys)]
    return sum(t)/xn

def main():
    resp = brfss.Respondents()
    resp.ReadRecords(data_dir='res')
    heights, weights = resp.GetHeightAndWeight()
    c1 = Cov(heights, weights)
    c2 = Cov(heights, heights)
    _, var = thinkstats.MeanVar(heights)
    print(c1, c2, var)

    print("-------------- ")
    # 官方方法2
    c3 = correlation.Cov(heights, weights)
    c4 = correlation.Cov(heights, heights)
    print(c3, c4, var)

if __name__ == "__main__":
    main()
