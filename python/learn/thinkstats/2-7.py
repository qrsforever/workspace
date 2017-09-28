#!/usr/bin/python3
# -*- coding: utf-8 -*-

import descriptive

def main():
    """
    <39
    """
    pool, firsts, others = descriptive.MakeTables("res")
    pmf = pool.pmf
    print("before pro(39) = ", pmf.Prob(39))
    for v in range(0, 39):
        try:
            pmf.Remove(v)
        except Exception as e:
            continue
    pmf.Normalize()
    print("after pro(39) = ", pmf.Prob(39))
    

if __name__ == "__main__":
    main()
