#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Babies
import Cdf

def Median(cdf):
    return cdf.Value(0.5)

def Interquartile(cdf):
    a = cdf.Value(0.25)
    b = cdf.Value(0.75)
    return a, b, b - a

def main():
    firsts, others, babies = Babies.PartitionBabies()
    cdf = Cdf.MakeCdfFromList(Babies.GetWightList(babies), name='babies')
    print("Median: ", Median(cdf))
    print("Interquartile: ", Interquartile(cdf))

if __name__ == "__main__":
    main()
