#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
斯皮尔曼秩相关系数(Spearman’s Rank Correlation)
请编写一个计算数据序列的秩的函数。
例如,设一个数据序列为 {7, 1, 2, 5},做秩转换后结果为 {4, 1, 2, 3}。
使用enumerate 和 sorted实现
"""
import brfss
import correlation

def ToRanks(t):
    """
    将数据序列转成秩
    """
    t1 = enumerate(t)
    s1 = sorted(t1, key=lambda t: t[1])
    t2 = enumerate(s1)
    s2 = sorted(t2, key=lambda t: t[1][0])
    return [t[0]+1 for t in s2]

def SpearmanCorr(xs, ys):
    """
    斯皮尔曼秩相关系数, 对异常值和变量分布不对称 不敏感
    """
    xs_r = ToRanks(xs)
    ys_r = ToRanks(ys)
    return correlation.Corr(xs_r, ys_r)

def main():
    # test
    t = [7, 1, 2, 5]
    print(ToRanks(t))
    
    # brfss
    resp = brfss.Respondents()
    resp.ReadRecords(data_dir='res')
    heights, weights = resp.GetHeightAndWeight()

    r1 = SpearmanCorr(heights, weights)
    r2 = correlation.SpearmanCorr(heights, weights)
    print("r1, r2 = ", r1, r2)


if __name__ == "__main__":
    main()
