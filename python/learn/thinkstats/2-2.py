#!/usr/bin/python3
# -*- coding: utf-8 -*-
   
import math
import first
import thinkstats

def Process(table):
    table.lengths = [p.prglength for p in table.records]
    table.n = len(table.lengths)
    table.mu, table.var = thinkstats.MeanVar(table.lengths)
    table.svar = math.sqrt(table.var)

def ProcessTables(*tables):
    for table in tables:
        Process(table)

if __name__ == "__main__":
    table, firsts, others = first.MakeTables("res") 
    ProcessTables(firsts, others)
    print("first table: n[{}] mu[{}] var[{}] svar[{}]".format(firsts.n, firsts.mu, firsts.var, firsts.svar))
    print("other table: n[{}] mu[{}] var[{}] svar[{}]".format(others.n, others.mu, others.var, others.svar))
