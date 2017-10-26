#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
为了研究样本数量对 p 值的影响,请读者试着去掉一半 NSFG 的数
据,再计算一下 p 值,并比较结果。如果去掉 3/4 的数据呢?提示:
使用 radom.sample 。
最少需要多少样本量才能保证差异有 5% 的显著性?如果要求有 1%
的显著性,又需要多少样本?
"""
import cumulative
import thinkstats
import time
import random
import hypothesis

def main():
    random.seed(time.clock())
    pool, firsts, others = cumulative.MakeTables()
    mean_var = thinkstats.MeanVar(pool.lengths)
    print('(Mean, Var) of pooled data', mean_var)

    print("--------------4/4 ")

    # NSFG原始数据
    hypothesis.RunTest('length-4-4', 
            pool.lengths,
            firsts.lengths, 
            others.lengths, 
            iters=1000,
            trim=False,
            partition=False)

    print("--------------3/4 ")

    # NSFG数据 3/4
    hypothesis.RunTest('length-3-4', 
            hypothesis.SampleWithoutReplacement(pool.lengths, int(pool.n * 0.75)),
            hypothesis.SampleWithoutReplacement(firsts.lengths, int(firsts.n * 0.75)),
            hypothesis.SampleWithoutReplacement(others.lengths, int(others.n * 0.75)),
            iters=1000,
            trim=False,
            partition=False)

    print("--------------2/4 ")

    # NSFG数据 1/2
    hypothesis.RunTest('length-half-2-4', 
            hypothesis.SampleWithoutReplacement(pool.lengths, int(pool.n * 0.5)),
            hypothesis.SampleWithoutReplacement(firsts.lengths, int(firsts.n * 0.5)),
            hypothesis.SampleWithoutReplacement(others.lengths, int(others.n * 0.5)),
            iters=1000,
            trim=False,
            partition=False)

    print("--------------1/4 ")

    # NSFG数据 1/4
    hypothesis.RunTest('length-half-1-4', 
            hypothesis.SampleWithoutReplacement(pool.lengths, int(pool.n * 0.25)),
            hypothesis.SampleWithoutReplacement(firsts.lengths, int(firsts.n * 0.25)),
            hypothesis.SampleWithoutReplacement(others.lengths, int(others.n * 0.25)),
            iters=1000,
            trim=False,
            partition=False)


if __name__ == "__main__":
    main()
