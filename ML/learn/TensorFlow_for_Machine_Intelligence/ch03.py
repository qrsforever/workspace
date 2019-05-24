#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file ch3.2.1.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-23 23:41:40

#############################  jupyter-vim map ######################################
# https://github.com/qrsforever/vim/blob/master/bundle/.configs/jupyter-vim_conf.vim
#   ,ji: import file
#   ,je: run cell
#   ,jj: run current line
#   ,jc: clear buffer; ju: update buffer; jq: quit buffer
#   ,jh: open buffer horizontally; jv: open buffer virtually
#   ,jf: !eog /tmp/jupyter_vim.png
#   ,jp: print <cword> variable; ,jt: print <cword> type
#   ,j1: output <cword> head(1), j2, j3, j4, j5 is also
#   ,j6: output <cword> tail(1), j7, j8, j9, j0 is also
#####################################################################################

import tensorflow as tf
import numpy as np

#####################################################################################
# <codecell> 3.2.1: 数据流
#####################################################################################

a = tf.constant(5, name='input_a')
b = tf.constant(3, name='input_b')
c = tf.multiply(a, b, name='mul_c')
d = tf.add(a, b, name='add_d')
e = tf.add(c, d, name='add_e')

sess = tf.Session()
sess.run(e)

writer = tf.summary.FileWriter('/tmp/tf', sess.graph)

writer.close()
sess.close()

#####################################################################################
# <codecell> 3.2.2: 张量
#####################################################################################

a = tf.constant([5,3], name='input_a')
b = tf.reduce_prod(a, name='prod_b')
c = tf.reduce_sum(a, name='sum_c')
d = tf.add(b, c, name='add_d')

sess = tf.Session()
sess.run(d)

writer = tf.summary.FileWriter('/tmp/tf', sess.graph)

writer.close()
sess.close()

#####################################################################################
# <codecell> 3.2.5: Graph
#####################################################################################

g1 = tf.get_default_graph()
g2 = tf.Graph()

with g1.as_default():
    sess = tf.Session(graph=g1)
    a = tf.constant([1, 2], name='input_a')
    b = tf.constant([2, 4], name='input_b')
    c = a + b
    sess.run(c)
    writer = tf.summary.FileWriter('/tmp/tf', sess.graph)
    writer.close()
    sess.close()

with g2.as_default():
    sess = tf.Session(graph=g2)
    e = tf.constant([1, 2], name='input_e')
    f = tf.constant([2, 4], name='input_f')
    g = e + f
    sess.run(g)
    writer = tf.summary.FileWriter('/tmp/tf', sess.graph)
    writer.close()
    sess.close()

#####################################################################################
# <codecell> 3.2.7: 占位节点
#####################################################################################

a = tf.placeholder(dtype=tf.int32, shape=(2), name='input_a')
b = tf.reduce_prod(a, name='prod_b')
c = tf.reduce_sum(a, name='sum_c')
d = tf.add(b, c, name='add_d')

sess = tf.Session()
input_dict = {a: np.array([5,3], dtype=np.int32)}
print(sess.run(fetches=d, feed_dict=input_dict))

#####################################################################################
# <codecell> 变量Variable
#####################################################################################

a = tf.Variable(3, trainable=True, name='var_a')
print(type(a))
# output: <class 'tensorflow.python.ops.variables.RefVariable'>
b = tf.constant(3, dtype=tf.int32, shape=[1], name='var_b')
print(type(b))
# output: <class 'tensorflow.python.framework.ops.Tensor'>

add = tf.add(a, 10, name='add')
print(type(add))
# output: <class 'tensorflow.python.framework.ops.Tensor'>
mul = tf.multiply(b, 20, name='mul')

zeros = tf.zeros(shape=[2, 2], dtype=tf.int32, name='zeros')
print(type(zeros))
# output: <class 'tensorflow.python.framework.ops.Tensor'>

ones = tf.ones(shape=[6], dtype=tf.float32)

init = tf.global_variables_initializer()
# output: <class 'tensorflow.python.framework.ops.Operation'>
print(type(init))
sess = tf.Session()
print(sess.run(init))
# output: None; 只初始化变量, 没有op操作

##

var1 = tf.Variable(1, name='var1')
var2 = tf.Variable(2, name='var2')

init1 = tf.variables_initializer([var1], name='init_var1')
sess = tf.Session()
sess.run(init1)

##

my_var = tf.Variable(1)
my_var_times_two = my_var.assign(my_var * 2)
# output: <class 'tensorflow.python.framework.ops.Tensor'>
init = tf.global_variables_initializer()
sess = tf.Session()
print(sess.run(init))
print(sess.run(my_var_times_two))  # 2
print(sess.run(my_var_times_two))  # 4
print(sess.run(my_var_times_two))  # 8

##

my_var1 = tf.Variable(1)
my_var2 = tf.Variable(2)
my_var_times_two = my_var2.assign(my_var1 * 2)
init = tf.global_variables_initializer()
sess = tf.Session()
print(sess.run(init))
print(sess.run(my_var_times_two)) # 2
print(sess.run(my_var_times_two)) # 2
print(sess.run(my_var_times_two)) # 2

##

sess.run(my_var1.assign_add(1)) # 2
sess.run(my_var1.assign_add(1)) # 3
sess.run(my_var1.assign_sub(1)) # 2
