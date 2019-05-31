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

def getvars():
    a = tf.get_variable('var_a', [3], initializer=tf.constant_initializer(1))
    b = tf.get_variable('var_b', [3], initializer=tf.constant_initializer(2))
    return a+b

var1 = getvars()
# var2 = getvars() # Error: Variable var_a already exists, disallowed.

with tf.variable_scope('scope1') as scope:
    # this var not use share
    var2 = getvars()
    # var3 = getvars() # Error: Variable scope1/var_a already exists, disallowed.
    # share方式一
    scope.reuse_variables()
    var3 = getvars()

with tf.variable_scope(scope, reuse=True):
    # share方式二
    var4 = getvars()

for co in tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES):
    print(co)
    # <tf.Variable 'var_a:0' shape=(3,) dtype=float32_ref>
    # <tf.Variable 'var_b:0' shape=(3,) dtype=float32_ref>
    # <tf.Variable 'scope1/var_a:0' shape=(3,) dtype=float32_ref>
    # <tf.Variable 'scope1/var_b:0' shape=(3,) dtype=float32_ref>

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(var1)) # [3. 3. 3.]
    print(sess.run(var2)) # [3. 3. 3.]
    print(sess.run(var3))
    print(sess.run(var4))
