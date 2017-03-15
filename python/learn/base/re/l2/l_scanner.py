#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
from collections import namedtuple

# pattern: Test : 50 = 100 - 10*5

NAME = r'(?P<NAME>[a-zA-Z][a-zA-Z0-9]*)'
TOK = r'(?P<TOK>:)'
NUM = r'(?P<NUM>\d+)'
EQ = r'(?P<EQ>=)'
SUB = r'(?P<SUB>-)'
MUL = r'(?P<MUL>\*)'
SP = r'(?P<SP>\s)'

pat1 = re.compile('|'.join([NAME, NUM, TOK, EQ, SUB, MUL, SP]))

def MyScanning(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for item in iter(scanner.match, None):
        yield Token(item.lastgroup, item.group())

for tok in MyScanning(pat1, 't1: 1 = 3 - 2'):
    print(tok)

for tok in MyScanning(pat1, 't1: 1 = 5 - 2*2'):
    print(tok)

# 包含关系 T2: 5 <= 10 (顺序：大的放前面)
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'

pat2 = re.compile('|'.join([NAME, TOK, NUM, EQ, LT, LE, SP]))
for tok in MyScanning(pat2, 't2: 5<=10'):
    print(tok)

pat2 = re.compile('|'.join([NAME, TOK, NUM, EQ, LE, LT, SP]))
for tok in MyScanning(pat2, 't2: 5<=10'):
    print(tok)


