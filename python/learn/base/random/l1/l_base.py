#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

#  print(dir(random))

values = [1, 3, 9, 8, 5, 4, 2]
print("1.choice: ", random.choice(values))
print("2.choice: ", random.choice(values))
print("1.sample: ", random.sample(values, 5))
print("2.sample: ", random.sample(values, 3))
print("before shuffle values = ", values)
random.shuffle(values)
print("after  shuffle values = ", values)

print("1.randint: ", random.randint(1, 9))
print("2.randint: ", random.randint(7, 9))

print("1.random float: ", random.random())
print("2.random float: ", random.random())
import os 
