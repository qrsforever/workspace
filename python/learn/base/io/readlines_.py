#!/usr/bin/python3
# -*- coding: utf-8 -*-

# <codecell>
with open ('./foo.txt', 'r') as f:
    print(f.readlines())
# out:['aaaaa\n', 'bbbbb\n', 'ccccc\n']

# <codecell>
with open ('./foo.txt', 'r') as f:
    print(list(map(lambda line: line.strip('\n'), f.readlines())))
# out: ['aaaaa', 'bbbbb', 'ccccc']
