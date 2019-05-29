#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file variables.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-29 14:11:39

import tensorflow as tf

#####################################################################################
# <codecell> create&init
#####################################################################################

sess = tf.Session()

##
var1 = tf.get_variable('myvar1', shape=[2,3,4], dtype=tf.float32)

# only name
print(tf.GraphKeys.GLOBAL_VARIABLES)
print(tf.GraphKeys.LOCAL_VARIABLES)
print(tf.GraphKeys.TRAINABLE_VARIABLES)

sess.run(var1.initializer)
print(sess.run(var1))

## 
var2 = tf.get_variable('myvar2', shape=[2,3], dtype=tf.float32,
        initializer=tf.zeros_initializer())

for co in tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES):
    print(co) # myvar1, myvar2 already add, but not init
print(sess.run(tf.report_uninitialized_variables())) # myvar2

init = tf.global_variables_initializer() # only is tensor, so myvar2 not init
print(sess.run(tf.report_uninitialized_variables())) # myvar2
sess.run(init)
print(sess.run(tf.report_uninitialized_variables())) # []

print(sess.run(var2))
# ouput
# [[0. 0. 0.]
#  [0. 0. 0.]]

## 
sess.close()

#####################################################################################
# <codecell> sharing
#####################################################################################

