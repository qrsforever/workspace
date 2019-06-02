#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file snowflake_neural_logic.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-06-01 17:19:23

################################  jupyter-vim #######################################
# https://github.com/qrsforever/vim/blob/master/bundle/.configs/jupyter-vim_conf.vim
# %pylab --no-import-all
#####################################################################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import tensorflow as tf
import memory_util
import sys

#####################################################################################
# <codecell> global
#####################################################################################

memory_util.vlog(1)

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.figsize'] = (12.0, 12.0)
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

tf.logging.set_verbosity(tf.logging.ERROR)

#####################################################################################
# <codecell> plot snowflake
#####################################################################################

# sess = tf.InteractiveSession()

inputs = tf.placeholder(dtype=tf.float32, shape=(2), name='inputs')

# 外圈半径
r1 = 10
# 内圈半径
r2 = r1/2 / np.cos(30*np.pi / 180)
# 位移
m = r1 + 5

# 调试打印
debug_ops = []
xs = []
ys = []

angles = np.array([i*np.pi / 180 for i in range(0, 360) if i % 30 == 0])
for i, angle in enumerate(angles, 0):
    if i % 2 == 1:
        xs.append(r1 * np.cos(angle) + m)
        ys.append(r1 * np.sin(angle) + m)
    else:
        xs.append(r2 * np.cos(angle) + m)
        ys.append(r2 * np.sin(angle) + m)

xs.append(xs[0])
ys.append(ys[0])

path = Path([(x,y) for x, y in zip(xs, ys)])
patch = patches.PathPatch(path, facecolor='grey', lw=0)
plt.gca().add_patch(patch)

plt.xlim(0, 40)
plt.ylim(0, 40)

# 计算线性方程参数k,b,计算新点
def plot_linear_equation(name, i, j, x1, x2):
    k = (ys[i] - ys[j]) / (xs[i] - xs[j])
    b = ys[i] - k * xs[i]
    print('%s: (%d, %d) k = %.2f, b = %.2f' % (name, i, j, k, b))
    xp = (x1, x2)
    yp = (k*x1+b, k*x2+b)
    plt.plot(xp, yp, color='g')
    plt.text(xp[1], yp[1], s = r'%s: $y = %.2f %s %.2f$' % (
        name, k, '' if b < 0 else '+', b))
    w = tf.constant((-1*k, 1), dtype=tf.float32)
    debug_ops.append(tf.print('%s: ' % name, w, b+tf.math.reduce_sum(w * inputs),
        output_stream=sys.stderr))
    return tf.cast(tf.nn.sigmoid(
        tf.math.reduce_sum(w * inputs) + b) > 0.5, tf.int32)

l1 = plot_linear_equation('l1', 3, 7, 4, 17)
l2 = plot_linear_equation('l2', 1, 9, 13, 26)
l3 = plot_linear_equation('l3', 5, 1, 4, 27)
l4 = plot_linear_equation('l4', 7, 11, 4, 27)
l5 = plot_linear_equation('l5', 3, 11, 13, 25)
l6 = plot_linear_equation('l6', 5, 9, 4, 17)

with tf.control_dependencies(debug_ops):
    data = tf.stack([l1, l2, l3, l4, l5, l6])
    with memory_util.capture_stderr() as stderr:
        print(data.eval(feed_dict={inputs:[15, 15]}))
        # l1.eval(feed_dict={inputs:[1, 15]})
        print(stderr.getvalue())

# sess.close() # noqa
