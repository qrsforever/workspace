#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

str = '''Train Epoch: 1	Train Iteration: 260	Time 1.609s / 20iters, (0.080)	Data load 0.036s / 20iters, (0.001794)
Learning rate = [0.1, 0.1]	Loss = {ce_loss: 2.3057, loss: 2.3117}
'''

print("#+++++++++++#")

RE_CLS_IC_TRAIN = re.compile(r'Train Epoch: (?P<epoch>\d+)\t'
                    r'Train Iteration: (?P<iters>\d+)\t'
                    r'Time (?P<batch_time_sum>\d+\.?\d*)s / (?P<batch_iters>\d+)iters, '
                    r'\((?P<batch_time_avg>\d+\.?\d*)\)\t'
                    r'Data load (?P<date_time_sum>\d+\.?\d*)s / (?P<_batch_iters>\d+)iters, '
                    r'\((?P<date_time_avg>\d+\.?\d*)\)\n'
                    r'Learning rate = (?P<learning_rate>.*)\t'
                    r'Loss = (?P<train_loss>.*)\n')


res = RE_CLS_IC_TRAIN.search(str)
if res:
    print(type(res.groupdict()['epoch']))
    print(res.groupdict()['iters'])
    print(res.groupdict()['batch_time_sum'])
    print(res.groupdict()['batch_iters'])
    print(res.groupdict()['batch_time_avg'])
    print(res.groupdict()['date_time_sum'])
    print(res.groupdict()['date_time_avg'])
    print(res.groupdict()['learning_rate'])
    print(res.groupdict()['train_loss'])

print("#+++++++++++#")

RE_CLS_IC_TRAIN = re.compile(r'Train Epoch: (?P<epoch>\d+)\t'
                    r'Train Iteration: (?P<iters>\d+)\t'
                    r'Time (?P<batch_time_sum>\d+\.?\d*)s / (?P<batch_iters>\d+)iters, '
                    r'\((?P<batch_time_avg>\d+\.?\d*)\)\t'
                    r'Data load (?P<date_time_sum>\d+\.?\d*)s / (?P<_batch_iters>\d+)iters, '
                    r'\((?P<date_time_avg>\d+\.?\d*)\)\n'
                    r'Learning rate = (?P<learning_rate>.*)\t'
                    r'Loss = .*loss: (?P<train_loss>\d+\.?\d*).*\n')

res = RE_CLS_IC_TRAIN.search(str)
if res:
    print(res.groupdict()['train_loss'])
