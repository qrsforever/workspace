#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import random
import thinkstats
import Cdf
import myplot

def patients_per_year(people, prob):
    patients = 0
    for p in range(people):
        r = (random.random() <= prob)
        if r:
            patients += 1

    return patients

def process(people, prob, years):
    patients = 0
    for y in range(years):
        patients += patients_per_year(people, prob)
    return patients

def Q1(people, prob, year):
    # 模拟次数
    simcount = 100
    results = []
    for c in range(simcount):
        results.append(process(people, prob, year))

    mu, var = thinkstats.MeanVar(results)
    sigma = math.sqrt(var)
    print("Q1: mu = %.3f, var = %.3f, sigma = %.3f" % (mu, var, sigma))
    return results

def Q2(results):
    results.sort()
    #  print(results)
    cdf = Cdf.MakeCdfFromList(results, name='cdf')
    myplot.Cdf(cdf)
    myplot.Show()
    p = [0.95, 0.99]
    for i in p:
        significant_value = cdf.Value(i)
        print("p:%4.2f significant_value = %d" % (i, significant_value))
    pass

def main():
    prob, year = 0.001, 10
    people = 100
    results = Q1(people, prob, year)
    Q2(results)

if __name__ == "__main__":
    main()
