#!/usr/bin/python3
# -*- coding: utf-8 -*-

import operator  
from functools import reduce
# scipy version >= 1.0.0
#  from scipy.special import perm

# combinatory
def mycomb(n, k):  
    return reduce(operator.mul, range(n-k+1, n+1)) / reduce(operator.mul, range(1, k+1))


# permutation
def myperm(n, k):  
    if n == k:
        return reduce(operator.mul, range(1,n+1))
    return reduce(operator.mul, range(1,n+1)) / reduce(operator.mul, range(1, n-k+1)) 

def main():
    print(mycomb(10, 5))
    print(myperm(4, 4))

if __name__ == "__main__":
    main()
