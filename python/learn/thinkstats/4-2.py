#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
假设不完全正确:婴儿在一天中各个时间出生的概率一样
"""

import BabyBoom
import Cdf
import myplot

def main():
    babies = BabyBoom.Babies()
    babies.ReadRecords(data_dir='res', n=None)
    lastmin = 0
    interval = []
    for item in babies.records:
        interval.append(item.minutes - lastmin)
        lastmin = item.minutes

    cdf = Cdf.MakeCdfFromList(interval, name='baby interval')
    myplot.Cdf(cdf, complement=False, transform=None)
    myplot.Show()

    # y轴取log(CCDF) : CCDF(X) = 1 - CDF(X)
    myplot.Clf()
    myplot.Cdf(cdf, complement=True, yscale='log')
    myplot.Show()

if __name__ == "__main__":
    main()

