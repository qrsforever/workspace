#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Bata Distribution (Bata分布)

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def testPdf():
    """
    http://user.qzone.qq.com/985612771/blog/1509866091
    β分布是一个取值在 [0, 1] 之间的连续分布，它由两个形态参数α和β的取值所刻画。
    β分布的形状取决于α和β的值。贝叶斯分析中大量使用了β分布。
    """
    a = 0.5
    b = 0.5
    xs = np.arange(0.01, 1, 0.01)
    ys = stats.norm.pdf(xs, a, b)
    plt.plot(xs, ys)
    plt.title('Beta: a=%.1f, b=%.1f' % (a,b))
    plt.xlabel('x')
    plt.ylabel('Probability density', fontsize=15)
    plt.show()

if __name__ == "__main__":
    testPdf()
