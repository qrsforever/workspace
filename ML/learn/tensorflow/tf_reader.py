#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file tf_reader.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-27 20:08:37

import tensorflow as tf


#####################################################################################
# <codecell> TextLineReader
#####################################################################################

# 构建文件名队列
filename_list = ['./res/a.csv', './res/b.csv', './res/c.csv']
# file_queue = tf.data.Dataset.list_files(filename_list)

filename_queue = tf.train.string_input_producer(["file0.csv", "file1.csv"])
