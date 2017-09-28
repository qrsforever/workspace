#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Babies
import Cdf
import myplot

mywt = 123.45

def main():
    firsts, others, babies = Babies.PartitionBabies()
    cdf_babies = Cdf.MakeCdfFromList(Babies.GetWightList(babies), name='babies')
    cdf_firsts = Cdf.MakeCdfFromList(Babies.GetWightList(firsts), name='firsts')
    cdf_others = Cdf.MakeCdfFromList(Babies.GetWightList(others), name='others')

    print("babies percentile rank: ", 100 * cdf_babies.Prob(mywt))
    print("firsts percentile rank: ", 100 * cdf_firsts.Prob(mywt))
    print("others percentile rank: ", 100 * cdf_others.Prob(mywt))

    myplot.Cdfs([cdf_babies, cdf_firsts, cdf_others])
    myplot.Show()

if __name__ == "__main__":
    main()
