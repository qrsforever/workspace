#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file tf_config.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-27 20:11:42

import os
import tensorflow as tf

# 设置警告级别
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

tf.logging.set_verbosity(tf.logging.ERROR)
