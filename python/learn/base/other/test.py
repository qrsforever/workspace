#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

aa = os.environ.get('AA', None)

print(aa)

testa = 0
testb = 0

if not aa and testa > -1:
    print('aaa')

def test_a():
    global testa, testb
    print(testa, id(testa))
    if testa == 0:
        testa = testa + 1
    print(testa, id(testa))

test_a()
test_a()
test_a()
test_a()

a, b = 1, 2
