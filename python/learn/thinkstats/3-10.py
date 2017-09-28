#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import Pmf
import Cdf
import myplot

def main():
    list = [100 * random.random() for i in range(1000)]
    pmf = Pmf.MakePmfFromList(list, name='pfm')
    cdf = Cdf.MakeCdfFromList(list, name='cdf')
    myplot.Pmf(pmf)
    myplot.Show()
    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Show()

if __name__ == "__main__":
    main()
