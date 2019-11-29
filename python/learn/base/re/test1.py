#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

a = 'TestLoss = {ce_loss: 2.3048, loss: 2.3048}'

res = re.search(r'TestLoss = .*loss: (?P<loss>\d+\.?\d*).*', a)

if res:
    print(res.groupdict()['loss'])
