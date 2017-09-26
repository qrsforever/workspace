#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import thinkstats

data=(1, 1, 1, 3, 3, 591)
def Pumpkin(data):
    mu, var = thinkstats.MeanVar(data)
    svar = math.sqrt(var)
    print("Pumpkin mean:{} variance:{} normal variance:{}".format(mu, var, svar))


if __name__ == "__main__":
    Pumpkin(data)
