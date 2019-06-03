#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file intro_convolution.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-06-03 20:52:26

################################  jupyter-vim #######################################
# https://github.com/qrsforever/vim/blob/master/bundle/.configs/jupyter-vim_conf.vim
# %pylab --no-import-all # noqa
#####################################################################################

import numpy as np
import matplotlib.pyplot as plt


#####################################################################################
# <codecell>
#####################################################################################

a = np.array([200, 200])
b = np.array([a, a])

kernel_horizonal = np.array([np.array([2, 2]), np.array([-2, 2])])

np.multiply(b, kernel_horizonal)
