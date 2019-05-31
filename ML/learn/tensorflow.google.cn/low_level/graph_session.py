#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file graph_session.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-30 18:22:35

################################  jupyter-vim #######################################
# https://github.com/qrsforever/vim/blob/master/bundle/.configs/jupyter-vim_conf.vim
# %pylab --no-import-all # noqa
#####################################################################################

import tensorflow as tf

#####################################################################################
# <codecell> naming scopse
#####################################################################################

c_0 = tf.constant(0, name='c') # Tensor("c:0", shape=(), dtype=int32)
c_1 = tf.constant(1, name='c') # Tensor("c_1:0", shape=(), dtype=int32)

with tf.name_scope('scope1'):
    c_2 = tf.constant(2, name='c') # Tensor("scope1/c:0", shape=(), dtype=int32)
    c_3 = tf.constant(3, name='c') # Tensor("scope1/c_1:0", shape=(), dtype=int32)

    with tf.name_scope('scopse2'):
        c_4 = tf.constant(4, name='c') # "scope1/scopse2/c:0"
        c_5 = tf.constant(5, name='c') # "scope1/scopse2/c_1:0"

    with tf.name_scope('scopse2'):
        c_6 = tf.constant(6, name='c') # "scope1/scopse2_1/c:0"
        c_7 = tf.constant(7, name='c') # "scope1/scopse2_1/c_1:0"


#####################################################################################
# <codecell> multiple graphs
#####################################################################################

print(tf.get_default_graph()) # 0x7feea5a98438

g1 = tf.Graph()
print(g1) # 0x7feea40f5160

with g1.as_default():
    print(tf.get_default_graph()) # 0x7feea40f5160
    c = tf.constant("node1 in g_1")
    sess1 = tf.Session()
    print(sess1.run(c))

print(tf.get_default_graph()) # 0x7feea5a98438

g2 = tf.Graph()
print(g2) # 0x7feea41c97b8

with g2.as_default():
    print(tf.get_default_graph()) # 0x7feea41c97b8
    d = tf.constant("node2 in g_2")
    sess2 = tf.Session()
    print(sess2.run(d))

sess3 = tf.Session(graph=g1)
sess3.run(c)
# sess3.run(d) #  Error: is not an element of this graph.
