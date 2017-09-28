#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Pmf
import first

def ProbEarly(pmf):
    """
    <= 37
    """
    rate = 0.0
    for w, p in pmf.Items():
        if w > 37:
            continue
        rate += p
    return rate

def ProbOnTime(pmf):
    """
    38, 39, 40
    """
    rate = 0.0
    for w, p in pmf.Items():
        if w > 37 and w < 41:
            rate += p
    return rate


def ProbLate(pmf):
    """
    >= 41
    """
    rate = 0.0
    for w, p in pmf.Items():
        if w < 41:
            continue
        rate += p
    return rate

def ProcessTables(table, firsts, others):
    firsts.prglengths = [p.prglength for p in firsts.records]
    others.prglengths = [p.prglength for p in others.records]
    #  table.prglengths.extend(firsts.prglengths)
    #  table.prglengths.extend(others.prglengths)


if __name__ == "__main__":
    alltbl, firsts, others = first.MakeTables(data_dir='res')
    ProcessTables(alltbl, firsts, others)
    #  alltbl_pmf = Pmf.MakePmfFromList(alltbl.prglengths, name='pool')
    firsts_pmf = Pmf.MakePmfFromList(firsts.prglengths, name='first')
    others_pmf = Pmf.MakePmfFromList(others.prglengths, name='other')

    print("ProbEarly(firsts) = ", ProbEarly(firsts_pmf))
    print("ProbOnTime(firsts) = ", ProbOnTime(firsts_pmf))
    print("ProbLate(firsts) = ", ProbLate(firsts_pmf))

    print("ProbEarly(others) = ", ProbEarly(others_pmf))
    print("ProbOnTime(others) = ", ProbOnTime(others_pmf))
    print("ProbLate(others) = ", ProbLate(others_pmf))
