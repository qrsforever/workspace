#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file tensors.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-29 13:20:31

#####################################################################################
# <codecell> header
#####################################################################################

import tensorflow as tf

#####################################################################################
# <codecell> Rank
#####################################################################################

mystr = tf.Variable("Hello", dtype=tf.string)
r1 = tf.rank(mystr) # Tensor
print(r1) # not correct, need sess.run()

myfloat = tf.Variable([1.0, 2.0], tf.float32)
r2 = tf.rank(myfloat)

myint = tf.Variable([[[1],[2]], [[3],[4]]], dtype=tf.int32)
r3 = tf.rank(myint)

sess = tf.Session()

print(sess.run(r1)) # 0
print(sess.run(r2)) # 1
print(sess.run(r3)) # 3

sess.close()

#####################################################################################
# <codecell> splice
#####################################################################################

myvar = tf.zeros(shape=[4,3,2], dtype=tf.int32)
rank = tf.rank(myvar)

sess = tf.Session()
print(sess.run(rank))  # 3
print(sess.run(myvar))
# output:
# [[[0 0]   |
#   [0 0]   |---> myvar[0]
#   [0 0]]  |
#
#  [[0 0]
#   [0 0]
#   [0 0]]
#
#  [[0 0]
#   [0 0]
#   [0 0]]
#
#    +----------> myvar[3, :, 0]
#    |
#  [[0 0]
#   [0 0]
#   [0 0]]]

mys1 = myvar[0]
print(sess.run(mys1))
# output:
# [[0 0]
#  [0 0]
#  [0 0]]

mys2 = myvar[1, 0, 0]
print(sess.run(mys2)) # 0

mys3 = myvar[3, :, 0]
print(sess.run(mys3)) # [0 0 0]

sess.close()

#####################################################################################
# <codecell> evaluating
#####################################################################################

constant = tf.constant([3,4,5], dtype=tf.int32)

myvar = constant * constant

float_tensor = tf.cast(myvar, dtype=tf.float32)

sess = tf.Session()
sess.as_default()
print(tf.get_default_session()) # none, but why, need with sess.as_default():

# same
float_tensor.eval(session=sess)
sess.run(float_tensor) # Out: array([ 9., 16., 25.], dtype=float32)

# placeholder eval must with feed_dict
pp = tf.placeholder(dtype=tf.int32)
myvar = pp + 1

with sess.as_default():
    print(tf.get_default_session())
    print(myvar.eval(feed_dict={pp:10}))

