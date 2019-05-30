#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file activation_functions.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-29 18:24:39

################################  jupyter-vim #######################################
# https://github.com/qrsforever/vim/blob/master/bundle/.configs/jupyter-vim_conf.vim
# %pylab --no-import-all # noqa
#####################################################################################

import numpy as np
import matplotlib.pyplot as plt

#####################################################################################
# <codecell> global
#####################################################################################

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.figsize'] = (16.0, 8.0)
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

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
        plt.annotate(ftxt, xy=(xpos, func(xpos)), xytext=xytext,
                textcoords='data', fontsize=16,
                arrowprops=dict(width=1, headwidth=6, headlength=8,
                    facecolor='r', shrink=0.05))
    if dfunc:
        plt.plot(xs, dfunc(xs), c='g', lw=3)
        plt.annotate(dftxt, xy=(dxpos, dfunc(dxpos)), xytext=dxytext,
                textcoords='data', fontsize=16,
                arrowprops=dict(width=1, headwidth=6, headlength=8,
                    facecolor='g', shrink=0.05))

#####################################################################################
# <codecell> Binary step (二元阶跃)
#####################################################################################

func = np.vectorize(lambda x: 1 if x > 0 else 0, otypes=[np.float])
dfunc = np.vectorize(lambda x: 0, otypes=[np.float])

text  = r"$ f(x) = \left\{\begin{array}{ccc}"
text += r" 0 & for & x\leq 0 \\ "
text += r" 1 & for & x> 0 "
text += r"\end{array}\right. $"

dtext  = r"$ f(x)' = \left\{\begin{array}{ccc}"
dtext += r"0 & for & x \neq 0 \\ "
dtext += r"? & for & x = 0 "
dtext += r"\end{array}\right. $"

display('binary step', (-0.1, 1.6),
        func, text, 2, (2.2, 0.5),
        dfunc, dtext, 0, (-3.5, 0.5)
        )


#####################################################################################
# <codecell> Piecewise Linear (线性分段)
#####################################################################################

xmin = -3.5
xmax = 3.5
w = 1/(xmax - xmin)
b = xmax*w

func = np.vectorize(lambda x: 1 if x > xmax else 0 if x < xmin else w*x+b,
        otypes=[np.float])
dfunc = np.vectorize(lambda x: 0 if x > xmax or x < xmin else w, otypes=[np.float])

text  = r"$ f(x) = \left\{\begin{matrix}"
text += r"0 & for & x < x_{min} \\ "
text += r"wx + b & for & x_{min} \leq x \leq x_{max} \\ "
text += r"1 & for & x > x_{max}"
text += r"\end{matrix}\right. \\ \\ \\ \\"
text += r"w=%.2f; b=%.2f; x_{min}=%.2f; x_{max}=%.2f $" % (w, b, xmin, xmax)

dtext  = r"$ f(x)' = \left\{\begin{matrix}"
dtext += r"0 & for & x < x_{min} \\ "
dtext += r"m & for & x_{min} \leq x \leq x_{max} \\ "
dtext += r"0 & for & x > x_{max}"
dtext += r"\end{matrix}\right. $"

display('piecewise linear', (-0.1, 1.6),
        func, text, -0.3, (-5.0, 1.0),
        dfunc, dtext, 2, (2.2, 0.5))


#####################################################################################
# <codecell> Bipolar
#####################################################################################

func = np.vectorize(lambda x: 1 if x > 0 else -1, otypes=[np.float])
dfunc = np.vectorize(lambda x: 0, otypes=[np.float])

text  = r"$ f(x) = \left\{\begin{matrix}"
text += r"-1 & for & x \leq 0 \\ "
text += r"1 & for & x > 0 "
text += r"\end{matrix}\right. $"

dtext  = r"$ f(x)' = \left\{\begin{matrix}"
dtext += r"0 & for & x \neq 0 \\ "
dtext += r"? & for & x = 0 "
dtext += r"\end{matrix}\right. $"

display('bipolar', (-1.5, 1.5),
        func, text, 1, (2, 0.5),
        dfunc, dtext, 0, (-4, 0.5)
        )


#####################################################################################
# <codecell> Sigmoid
#####################################################################################

def sigmoid_func(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_dfunc(x):
    fx = sigmoid_func(x)
    return fx * (1 - fx)

text = r"$ f(x) = \dfrac{1}{1 + e^{-x}} $"
dtext = r"$ f(x)' = f(x) * (1-f(x)) $"

display('sigmiod', (-0.2, 1.2),
        sigmoid_func, text, 1, (2, 0.5),
        sigmoid_dfunc, dtext, -1, (-5, 0.5))

#####################################################################################
# <codecell> Bipolar Sigmoid
#####################################################################################

def bisigmoid_func(x):
    return (1 - np.exp(-x)) / (1 + np.exp(-x))

def bisigmoid_dfunc(x):
    return 2 * np.exp(x) / ((np.exp(x) + 1) ** 2)

text = r"$ f(x) = \dfrac{1-e^{-x}}{1+e^{-x}} $"
dtext = r"$ f(x)' = \dfrac{2e^x}{(e^x + 1)^2} $"

display('bipolar sigmiod', (-1.2, 1.2),
        bisigmoid_func, text, 0.2, (1, -0.5),
        bisigmoid_dfunc, dtext, -3, (-4, 0.5))


#####################################################################################
# <codecell> Hyperbolic Tangent, TanH (双曲正切)
#####################################################################################

def tanh_func(x):
    return 2 / (1 + np.exp(-2 * x)) - 1

def tanh_dfunc(x):
    fx = tanh_func(x)
    return 1 - fx ** 2

text = r"$ f(x) = \dfrac{1}{1 + e^{-2x}} - 1 $"
dtext = r"$ f(x)' = 1 - f(x)^2 $"

display('hyperbolic tangent', (-1.2, 1.2),
        tanh_func, text, 0.2, (1, -0.5),
        tanh_dfunc, dtext, -1.0, (-4, 0.6))


#####################################################################################
# <codecell> Arctangent, Arctan
#####################################################################################

def arctan_func(x):
    return np.arctan(x)

def arctan_dfunc(x):
    return 1 / (1 + x ** 2)

text = r"$ f(x) = tan^{-1}x $"
dtext = r"$ f(x)' = \dfrac{1}{1+x^2} $"

display('arctangent', (-1.5, 1.5),
        arctan_func, text, 0.2, (1, -0.5),
        arctan_dfunc, dtext, -1.0, (-4, 1.2))


#####################################################################################
# <codecell> Rectified Linear Units, ReLU
#####################################################################################

relu_func = np.vectorize(lambda x: x if x > 0 else 0, otypes=[np.float])

relu_dfunc = np.vectorize(lambda x: 1 if x > 0 else 0, otypes=[np.float])

text  = r"$ f(x) = \left\{\begin{matrix}"
text += r"0 & for & x \leq 0 \\ "
text += r"x & for & x > 0 "
text += r"\end{matrix}\right. $"

dtext  = r"$ f(x)' = \left\{\begin{matrix}"
dtext += r"0 & for & x \leq 0 \\ "
dtext += r"1 & for & x > 0 "
dtext += r"\end{matrix}\right. $"

display('relu', (-0.5, 1.5),
        relu_func, text, 0.6, (1.8, 0.5),
        relu_dfunc, dtext, -2.0, (-3.2, 0.5))


#####################################################################################
# <codecell> Leaky Rectified Linear Units, Leaky ReLU
#####################################################################################

a = 0.1

lrelu_func = np.vectorize(lambda x: x if x > 0 else a*x, otypes=[np.float])

lrelu_dfunc = np.vectorize(lambda x: 1 if x > 0 else a, otypes=[np.float])

text  = r"$ f(x) = \left\{\begin{matrix}"
text += r"ax & for & x \leq 0 \\ "
text += r"x & for & x > 0 "
text += r"\end{matrix}\right. \\ \\ \\"
text += r"a=%.2f $" % a

dtext  = r"$f(x)' = \left\{\begin{matrix}"
dtext += r"a & for & x \leq 0 \\ "
dtext += r"1 & for & x > 0 "
dtext += r"\end{matrix}\right. $"

display('leaky relu', (-0.5, 1.5),
        lrelu_func, text, 0.6, (1.8, 0.5),
        lrelu_dfunc, dtext, -2.0, (-3.2, 0.5))


#####################################################################################
# <codecell> Exponential Linear Units, ELU
#####################################################################################

a = 0.5

elu_func = np.vectorize(lambda x: x if x > 0 else a*(np.exp(x)-1), otypes=[np.float])

elu_dfunc = np.vectorize(lambda x: 1 if x > 0 else a*np.exp(x), otypes=[np.float])

text  = r"$ f(x) = \left\{\begin{matrix}"
text += r"a(e^x-1) & for & x \leq 0 x \\ "
text += r"x & for & x > 0 "
text += r"\end{matrix}\right. $"

dtext  = r"$ f(x)' = \left\{\begin{matrix}"
dtext += r"f(x) + a & for & x \leq 0 \\ "
dtext += r"1 & for & x > 0 "
dtext += r"\end{matrix}\right.  \\ \\ \\"
dtext += r"a=%.2f $" % a

display('elu', (-0.5, 1.5),
        elu_func, text, 0.6, (1.8, 0.5),
        elu_dfunc, dtext, -0.5, (-4.5, 0.5))


#####################################################################################
# <codecell> SoftPlus
#####################################################################################

def softplus_func(x):
    return np.log(1+np.exp(x))

def softplus_dfunc(x):
    return 1/(1+np.exp(-x))

text = r"$ f(x) = ln(1 + e^x) $"

dtext = r"$ f(x)' = \dfrac{1}{1 + e^{-x}} $"

display('softplus', (-0.5, 1.5),
        softplus_func, text, 0.6, (1.8, 0.5),
        softplus_dfunc, dtext, -2.0, (-3.2, 0.5))
