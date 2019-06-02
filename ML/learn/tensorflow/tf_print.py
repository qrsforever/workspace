#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file tf_print.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-06-02 15:40:55

################################  jupyter-vim #######################################
# https://github.com/qrsforever/vim/blob/master/bundle/.configs/jupyter-vim_conf.vim
# %pylab --no-import-all # noqa
#####################################################################################

# https://github.com/yaroslavvb/memory_util

import sys
import tensorflow as tf
import memory_util

memory_util.vlog(1)

sess = tf.Session()
with sess.as_default():
    tensor = tf.range(10)
    print_op = tf.print("tensors:", tensor, {'2': tensor * 2}, output_stream=sys.stderr)
    with tf.control_dependencies([print_op]):
        tripled_tensor = tensor * 3
        with memory_util.capture_stderr() as stderr:
            print(sess.run(tripled_tensor))
            print(stderr.getvalue())
