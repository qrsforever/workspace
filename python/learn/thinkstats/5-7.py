#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import brfss
import thinkstats

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

if __name__ == "__main__":
    main()
