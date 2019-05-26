#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt

print(plt.style.available)
plt.style.use('ggplot')

print(matplotlib.matplotlib_fname())

# 设置中文和负号正常显示
plt.rcParams['font.sans-serif'] = 'monospace'
plt.rcParams['axes.unicode_minus'] = False


# ioff() # Turn interactive plotting off
# ion() # Turn interactive plotting on
plt.ion() # 自动显示出图片

