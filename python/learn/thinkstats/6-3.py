#!/usr/bin/python3
# -*- coding: utf-8 -*-

import skewness
import irs

def main():
    data = irs.ReadIncomeFile(filename='res/08in11si.csv')
    hist, pmf, cdf = irs.MakeIncomeDist(data)
    mean, median = cdf.Mean(), cdf.Percentile(50)
    print("irs mean = %.3f, median = %.3f, %.3f%% people low mean" % (mean, median, cdf.Prob(mean)*100))
    skewness.show_skewness(l=pmf, name='irs income', show=True)

if __name__ == "__main__":
    main()
