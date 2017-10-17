#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import Babies
import thinkstats
import Pmf
import myplot
import skewness

def Skewness(d):
    n = len(d)
    mean = thinkstats.Mean(d)
    
    m2 = 0
    m3 = 0
    for x in d:
        t = x - mean
        m2 += t**2
        m3 += t**3
    m2 /= n
    m3 /= n

    return m3 / (m2**(3/2))

def PearsonSkewness(d):
    n = len(d)
    sorted(d)
    mean, var = thinkstats.MeanVar(d)
    sigma = math.sqrt(var)
    median = 0
    if n % 2: 
        median = d[n/2 + 1]
    else:
        median = (d[int(n/2)] + d[int((n+1)/2)]) / 2

    print("median = %.3f", median)
    return 3*(mean - median)/sigma

def main():
    firsts, others, babies = Babies.PartitionBabies()
    d = Babies.GetPregnacyList(babies)
    hist = Pmf.MakeHistFromList(d, name='pregnacylist')
    myplot.Hist(hist)
    myplot.Show()

    g1 = Skewness(d)
    gp = PearsonSkewness(d)

    print("g1 = %.3f, gp = %.3f" % (g1, gp))
    skewness.show_skewness(l=d, name='pregnancy skewness')
    

if __name__ == "__main__":
    main()
