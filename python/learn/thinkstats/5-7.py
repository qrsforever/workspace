#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import brfss
import thinkstats
import myplot
import Pmf, Cdf

def main():
    resp = brfss.Respondents()
    resp.ReadRecords(data_dir='res')
    d = resp.SummarizeHeight()

    man_d = d[1]
    lady_d = d[2]

    # 男性的mu, var, sigma, 变异系数CV
    man_mu, man_var = thinkstats.TrimmedMeanVar(man_d)
    man_sigma = math.sqrt(man_var)
    man_cv = man_sigma/man_mu
    print("man: mu = %.3f, var = %.3f, sigma = %.3f, cv = %.3f" % (man_mu, man_var, man_sigma, man_cv))

    # 女性的mu, var, sigma, 变异系数CV
    lady_mu, lady_var = thinkstats.TrimmedMeanVar(lady_d)
    lady_sigma = math.sqrt(lady_var)
    lady_cv = lady_sigma/lady_mu
    print("lady: mu = %.3f, var = %.3f, sigma = %.3f, cv = %.3f" % (lady_mu, lady_var, lady_sigma, lady_cv))

    # 男性, 女性Hist分布
    man_hist = Pmf.MakeHistFromList(man_d, name='man hist')
    myplot.Hist(man_hist)
    myplot.Show()

    myplot.Clf()

    lady_hist = Pmf.MakeHistFromList(lady_d, name='lady hist')
    myplot.Hist(lady_hist)
    myplot.Show()

    myplot.Clf()

    # 男性, 女性Pmf分布
    man_pmf = Pmf.MakePmfFromHist(man_hist, name='man pmf')
    myplot.Pmf(man_pmf)
    myplot.Show()

    myplot.Clf()

    lady_pmf = Pmf.MakePmfFromHist(lady_hist, name='lady pmf')
    myplot.Pmf(lady_pmf)
    myplot.Show()

    myplot.Clf()

    # 男性/女性Cdf累积分布
    man_cdf = Cdf.MakeCdfFromPmf(man_pmf, name='man cdf')
    lady_cdf = Cdf.MakeCdfFromPmf(lady_pmf, name='lady cdf')
    myplot.Cdfs((man_cdf, lady_cdf), complement=False, transform=None)
    myplot.Show()


if __name__ == "__main__":
    main()
