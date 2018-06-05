#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np

sess = tf.Session();

def test_1():
    x_vals = np.array([1., 3., 5., 7., 9.])
    x_data = tf.placeholder(tf.float32)
    m_const = tf.constant(3.)
    my_product = tf.multiply(x_data, m_const)
    for x_val in x_vals:
        print(sess.run(my_product, feed_dict={x_data: x_val}))


def test_2():
    pass


