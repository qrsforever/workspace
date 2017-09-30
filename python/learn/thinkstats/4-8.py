#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import Babies
import Cdf
import myplot
import thinkstats
import erf

if __name__ == "__main__":
    firsts, others, babies = Babies.PartitionBabies()
    preglengths = Babies.GetPregnacyList(babies)
    mu = thinkstats.Mean(preglengths)
    sigma = math.sqrt(thinkstats.Var(preglengths, mu))
    print("mu = %.3f sigma = %.3f" % (mu, sigma))

    cdf0 = Cdf.MakeCdfFromList(preglengths, name='cdf0')

    ys = [erf.NormalCdf(x, mu=mu, sigma=sigma) for x in preglengths]
    cdf1 = Cdf.Cdf(preglengths, ys, 'cdf1')

    myplot.Cdf(cdf1, complement=False, transform=None)
    myplot.Cdfs([cdf0, cdf1], complement=False, transform=None)
    myplot.Show()
    # TODO wrong
