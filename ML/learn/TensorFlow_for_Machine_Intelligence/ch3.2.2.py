#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file ch3.2.2.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-23 23:51

#############################  jupyter-vim map ######################################
# https://github.com/qrsforever/vim/blob/master/bundle/.configs/jupyter-vim_conf.vim
#   ,ji: import file
#   ,je: run cell
#   ,jj: run current line
#   ,jc: clear buffer; ju: update buffer; jq: quit buffer
#   ,jh: open buffer horizontally; jv: open buffer virtually
#   ,jf: !eog /tmp/jupyter_vim.png
#   ,jp: print <cword> variable
#   ,j1: output <cword> head(1), j2, j3, j4, j5 is also
#   ,j6: output <cword> tail(1), j7, j8, j9, j0 is also
#####################################################################################

import tensorflow as tf


#####################################################################################
# <codecell> 定义数据流
#####################################################################################
a = tf.constant([5,3], name='input_a')
b = tf.reduce_prod(a, name='prod_b')
c = tf.reduce_sum(a, name='sum_c')
d = tf.add(b, c, name='add_d')

#####################################################################################
# <codecell> 运行数据流
#####################################################################################
sess = tf.Session()
sess.run(d)

#####################################################################################
# <codecell> tensorboard --logdir=/tmp/tf
#####################################################################################
writer = tf.summary.FileWriter('/tmp/tf', sess.graph)

#####################################################################################
# <codecell> 关闭资源
#####################################################################################
writer.close()
sess.close()
