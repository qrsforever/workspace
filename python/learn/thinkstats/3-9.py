#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import Babies
import Cdf
import myplot

def Sample(cdf, n):
    #random.random() 返回随机生成的一个实数，它在[0,1)范围内。 
    return [cdf.Value(random.random()) for i in range(n)]

def WeightRandomSample(cdf, n = 1000):
    return cdf.Sample(n)

def main():
    firsts, others, babies = Babies.PartitionBabies()
    cdf0 = Cdf.MakeCdfFromList(Babies.GetWightList(babies), name='cdf0')
    print("Sample(cdf, 10) : ", Sample(cdf0, 10))
    
    d1 = WeightRandomSample(cdf0, 100)
    cdf1 = Cdf.MakeCdfFromList(d1, name='cdf1')

    d2 = WeightRandomSample(cdf0, 1000)
    cdf2 = Cdf.MakeCdfFromList(d2, name='cdf2')

    myplot.Cdfs([cdf0, cdf1, cdf2], complement=False, transform=None)
    myplot.Show()


if __name__ == "__main__":
    main()
