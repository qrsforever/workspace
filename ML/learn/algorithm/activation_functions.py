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

##

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
# <codecell> Binary step (二元阶跃)
#####################################################################################

step_func = np.vectorize(lambda x: 1 if x > 0 else 0, otypes=[np.float])

f_text  = r'$ f(x) = \left\{\begin{array}{ccc}'
f_text += r' 0 & for & x\leq 0 \\ '
f_text += r' 1 & for & x> 0 '
f_text += r'\end{array}\right. $'

display('binary step', (-0.1, 1.6),
        step_func, f_text, 2, (2.2, 0.5))


#####################################################################################
# <codecell> Piecewise Linear (线性分段)
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


#####################################################################################
# <codecell> Bipolar
#####################################################################################

bipolar_func = np.vectorize(lambda x: 1 if x > 0 else -1, otypes=[np.float])

display('bipolar', (-1.5, 1.5),
        bipolar_func, 'bipolar_func', 1, (2, 0.5))


#####################################################################################
# <codecell> Sigmoid
#####################################################################################

def sigmoid_func(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_dfunc(x):
    fx = sigmoid_func(x)
    return fx * (1 - fx)

display('sigmiod', (-0.2, 1.2),
        sigmoid_func, 'sigmoid_func', 1, (2, 0.5),
        sigmoid_dfunc, 'sigmoid_dfunc', -1, (-2, 0.5))

#####################################################################################
# <codecell> Bipolar Sigmoid
#####################################################################################

def bisigmoid_func(x):
    return (1 - np.exp(-x)) / (1 + np.exp(-x))

def bisigmoid_dfunc(x):
    return 2 * np.exp(x) / ((np.exp(x) + 1) ** 2)

display('bisigmiod', (-1.2, 1.2),
        bisigmoid_func, 'bisigmoid_func', 0.2, (1, -0.5),
        bisigmoid_dfunc, 'bisigmoid_dfunc', -5, (-4, 0.5))


#####################################################################################
# <codecell> Hyperbolic Tangent, TanH (双曲正切)
#####################################################################################

def tanh_func(x):
    return 2 / (1 + np.exp(-2 * x)) - 1

def tanh_dfunc(x):
    fx = tanh_func(x)
    return 1 - fx ** 2

display('hyperbolic tangent', (-1.2, 1.2),
        tanh_func, 'aaa', 0.2, (1, -0.5),
        tanh_dfunc, 'bbb', -1.0, (-2, 0.5))


#####################################################################################
# <codecell> Arctangent, Arctan
#####################################################################################

def arctan_func(x):
    return np.arctan(x)

def arctan_dfunc(x):
    return 1 / (1 + x ** 2)

display('arctangent', (-1.5, 1.5),
        arctan_func, 'aaa', 0.2, (1, -0.5),
        arctan_dfunc, 'bbb', -1.0, (-2, 0.5))


#####################################################################################
# <codecell> Rectified Linear Units, ReLU
#####################################################################################

relu_func = np.vectorize(lambda x: x if x > 0 else 0, otypes=[np.float])

relu_dfunc = np.vectorize(lambda x: 1 if x > 0 else 0, otypes=[np.float])

display('relu', (-0.5, 1.5),
        relu_func, 'aaa', 0.6, (1.8, 0.5),
        relu_dfunc, 'bbb', -2.0, (-3.2, 0.5))


#####################################################################################
# <codecell> Leaky Rectified Linear Units, Leaky ReLU
#####################################################################################

a = 0.1

lrelu_func = np.vectorize(lambda x: x if x > 0 else a*x, otypes=[np.float])

lrelu_dfunc = np.vectorize(lambda x: 1 if x > 0 else a, otypes=[np.float])

display('leaky relu', (-0.5, 1.5),
        lrelu_func, 'aaa', 0.6, (1.8, 0.5),
        lrelu_dfunc, 'bbb', -2.0, (-3.2, 0.5))


#####################################################################################
# <codecell> Exponential Linear Units, ELU
#####################################################################################

a = 0.5

elu_func = np.vectorize(lambda x: x if x > 0 else a*(np.exp(x)-1), otypes=[np.float])

elu_dfunc = np.vectorize(lambda x: 1 if x > 0 else a*np.exp(x), otypes=[np.float])

display('elu', (-0.5, 1.5),
        elu_func, 'aaa', 0.6, (1.8, 0.5),
        elu_dfunc, 'bbb', -2.0, (-3.2, 0.5))


#####################################################################################
# <codecell> SoftPlus
#####################################################################################

def softplus_func(x):
    return np.log(1+np.exp(x))

def softplus_dfunc(x):
    return 1/(1+np.exp(-x))

display('softplus', (-0.5, 1.5),
        softplus_func, 'aaa', 0.6, (1.8, 0.5),
        softplus_dfunc, 'bbb', -2.0, (-3.2, 0.5))
