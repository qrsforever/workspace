#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file tf_stack_unstack.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-27 19:44:06

#############################  jupyter-vim map ######################################
# https://github.com/qrsforever/vim/blob/master/bundle/.configs/jupyter-vim_conf.vim
#   ,ji: import file; ,je: run cell; ,jj: run current line
#   ,jc: clear buffer; ju: update buffer; jq: quit buffer
#   ,jh: open buffer horizontally; jv: open buffer virtually
#   ,jp: print <cword> variable; ,jt: print <cword> type
#   ,j1: output <cword> head(1), j2, j3, j4, j5 is also
#   ,j6: output <cword> tail(1), j7, j8, j9, j0 is also
#####################################################################################

import tensorflow as tf


#####################################################################################
# <codecell> stack
#####################################################################################

## 

a = tf.constant([1,2,3])
b = tf.constant([2,3,4])

##

c = tf.stack([a, b], axis=0) # c: <class 'tensorflow.python.framework.ops.Tensor'>

with tf.Session() as sess:
    print(sess.run(c))

# output:
# [[1 2 3]
#  [2 3 4]]
  
##

d = tf.stack([a, b], axis=1)

with tf.Session() as sess:
    print(sess.run(d))

# output:
# [[1 2]
#  [2 3]
#  [3 4]]

#####################################################################################
# <codecell> unstack
#####################################################################################

##

e = tf.unstack(c, num=2, axis=0) # <class 'list'>

print(type(e[0])) # <class 'tensorflow.python.framework.ops.Tensor'>

f = tf.unstack(c, num=3, axis=1) # <class 'list'>

with tf.Session() as sess:
    print(sess.run(e))
    print(sess.run(f))
    print(sess.run([e, f]))
