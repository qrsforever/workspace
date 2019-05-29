#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file activation_functions.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-29 18:24:39

# run this file using jupyter-vim

#####################################################################################
# <codecell> header
#####################################################################################

import os
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline # not work in jupyter-vim

#####################################################################################
# <codecell> global
#####################################################################################

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False # 负号正常显示
plt.rcParams['figure.figsize'] = (16.0, 8.0)
plt.rcParams['text.usetex'] = True

xs = np.arange(-6, 6, 0.01)

## plot.show

def display(title, yaxis,
        func, ftxt = None, xpos=0, xytext=(0,0),
        dfunc=None, dftxt=None, dxpos=None, dxytext=None):

    plt.title(title, fontsize='xx-large', fontweight='bold', color='b')
    plt.ylim(yaxis)
    plt.locator_params('both', nbins=8) # 调整x,y坐标系的刻度划分
    plt.xticks(fontsize=14) # 设置坐标刻度字体
    plt.yticks(fontsize=14)
    plt.axhline(lw=1, c='black') # 轴线设置
    plt.axvline(lw=1, c='black')
    plt.grid(alpha=0.4, ls='-.')
    plt.box(on=None)
    plt.plot(xs, func(xs), c='r', lw=3)

    if ftxt:
        plt.annotate(ftxt, xy=(xpos, func(xpos)), xytext=xytext, fontsize=16,
                arrowprops=dict(width=1,headwidth=6,facecolor='black',shrink=0.05))
    if dfunc:
        plt.plot(xs, dfunc(xs), c='g', lw=3)

    if dftxt:
        plt.annotate(dftxt, xy=(dxpos, dfunc(dxpos)), xytext=dxytext, fontsize=16,
                arrowprops=dict(width=1,headwidth=6,facecolor='black',shrink=0.05))

    # jupyter-vim can not plot inline, so using eog
    plt.savefig('/tmp/af.png')
    os.system('eog /tmp/af.png')


#####################################################################################
# <codecell> binary step (二元阶跃)
#####################################################################################

step_func = np.vectorize(lambda x: 1 if x > 0 else 0, otypes=[np.float])

f_text  = r'$ f(x) = \bigg\{\begin{array}{ccc}'
f_text += r' 0 & for & x\leq 0 \\ '
f_text += r' 1 & for & x> 0 '
f_text += r'\end{array} $'

display('binary step', (-0.1, 1.6),
        step_func, f_text, 2, (2.2, 0.5))


#####################################################################################
# <codecell> piecewise linear (线性分段)
#####################################################################################

xmin = -3.5
xmax = 3.5
w = 1/(xmax - xmin)
b = xmax*w

piece_func = np.vectorize(lambda x: 1 if x > xmax else 0 if x < xmin else w*x+b,
        otypes=[np.float])
piece_dfunc = np.vectorize(lambda x: w, otypes=[np.float])

display('piecewise linear', (-0.1, 1.6),
        piece_func, -2, (-2.2, 0.5), 'aaaa',
        piece_dfunc, 2, (2.2, 0.5), 'bbbb')
