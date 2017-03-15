#!/usr/bin/python3
# -*- coding: utf-8 -*-

a = ['aaa', 'bbb', 'ccc']
a1='aaa'
a2='bbb'
a3= a1 + ':' + a2

print(a1, a2, sep=':')
print(':'.join(a))
print(a3)
print('{}:{}'.format(a1, a2))

def sample():
    yield 'aaaa'
    yield 'bbbb'
    yield 'cccc'

print([str(n) for n in sample()])
print(":".join(sample()))
