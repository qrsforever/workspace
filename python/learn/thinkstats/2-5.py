#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Pmf
import thinkstats

def PmfMean(pmf):
    mu = 0.0
    for key, val in pmf.Items():
        mu += key * val
    return mu

def PmfVar(pmf, mu):
    var = 0.0
    for key, val in pmf.Items():
        var += val * (key - mu)**2
    return var

if __name__ == "__main__":
    data=(1, 1, 1, 3, 3, 591)
    mu, var = thinkstats.MeanVar(data)
    print("Mean:{} Var:{}".format(mu, var))
    print("-------------- ")
    pmf = Pmf.MakePmfFromList(data, name='test')
    mu = PmfMean(pmf)
    var = PmfVar(pmf, mu)
    print("Mean:{} Var:{}".format(mu, var))
    print("-------------- ")
    print("Mean:{} Var:{}".format(pmf.Mean(), pmf.Var(mu=None)))
