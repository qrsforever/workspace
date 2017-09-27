#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy
import Pmf

def RemainingLifetime(pmf, age):
    newdata = {}
    for key, value in pmf.Items():
        if key < age:
            continue
        newdata[key] = value
    return Pmf.MakePmfFromDict(newdata, name='lifetime')

if __name__ == "__main__":
    data = numpy.random.randint(45 , high=75, size=60)
    pmf = Pmf.MakePmfFromList(data, name='lifetime')
    print("pmf.Total() = ", pmf.Total())
    print("pmf.MaxLike() = ", pmf.MaxLike())
    print("pmf.GetDict() = ", pmf.GetDict())
    print("pmf.Prob(55) = ", pmf.Prob(55, default=0))
    print("-------------- ")
    pmf = RemainingLifetime(pmf, 55)
    print("pmf.Total() = ", pmf.Total())
    print("pmf.MaxLike() = ", pmf.MaxLike())
    print("pmf.GetDict() = ", pmf.GetDict())
    print("pmf.Prob(55) = ", pmf.Prob(55, default=0))
