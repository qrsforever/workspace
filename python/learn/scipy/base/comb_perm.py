#!/usr/bin/python3
# -*- coding: utf-8 -*-

import operator  
from functools import reduce

# combinatory
def comb(n, k):  
    return reduce(operator.mul, range(n-k+1, n+1)) / reduce(operator.mul, range(1, k+1))


# permutation
def perm(n, k):  
    if n == k:
        return reduce(operator.mul, range(1,n+1))
    return reduce(operator.mul, range(1,n+1)) / reduce(operator.mul, range(1, n-k+1)) 

def main():
    print(comb(10, 5))
    print(perm(4, 4))

if __name__ == "__main__":
    main()
