#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

(last_key, max_value) = (None, -9999)

# input data is alreay sort
for line in sys.stdin:
    (key, val) = line.strip().split("\t")
    if last_key and last_key != key:
        print("{}\t{}".format(last_key, max_value))
        (last_key, max_value) = (key, int(val))
    else:
        (last_key, max_value) = (key, max(max_value, int(val)))

if last_key:
    print("{}\t{}".format(last_key, max_value))
