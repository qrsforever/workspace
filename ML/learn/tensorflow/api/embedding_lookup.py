#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file embedding_lookup.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-30 23:10:03

################################  jupyter-vim #######################################
# https://github.com/qrsforever/vim/blob/master/bundle/.configs/jupyter-vim_conf.vim
# %pylab --no-import-all # noqa
#####################################################################################

import tensorflow as tf

sess = tf.InteractiveSession()

##

#####################################################################################
# <codecell> 简单实例(single tensor)
#####################################################################################

params = tf.constant([10, 30, 20, 40])

print(params.eval())

ids = tf.constant([0, 1, 2, 3])
print(tf.nn.embedding_lookup(params, ids).eval()) # [10 30 20 40]

ids = tf.constant([0, 2, 1])
print(tf.nn.embedding_lookup([params], ids).eval()) # [10 20 30]

try:
    ids = tf.constant([4, 2, 1, 3])
    print(tf.nn.embedding_lookup([params], ids).eval()) # throw Exception
except Exception as e:
    print(e.message) # Error: 4 is not in [0, 4)


#####################################################################################
# <codecell> 多个Tensor (list)
#####################################################################################

params1 = tf.constant([1, 2])
params2 = tf.constant([10, 20])
params3 = tf.constant([15, 5])
params = [params1, params2, params3]

print(len(params)) # 3 > 1
print(tf.convert_to_tensor(params).eval())
# output:
# [[ 1   2]
#  [10  20]
#  [15   5]]

ids = tf.constant([0, 1, 2, 3, 5])
print(tf.nn.embedding_lookup(params, ids).eval()) # [1 10 15 2 5]

# index 0 correponses to the first element of the first tensor, so is 1
# index 1 correponses to the first element of the second tensor, so is 10
# index 2 correponses to the first element of the third tensor, so is 15
# index 3 correponses to the second element of the first tensor, so is 2
# index 4 correponses to the second element of the third tensor, so is 5


#####################################################################################
# <codecell> 策略(模与除)
#####################################################################################

params1 = tf.constant([1, 2])
params2 = tf.constant([10, 20])
ids = tf.constant([0, 1, 2, 3])

mod = tf.nn.embedding_lookup([params1, params2], ids, partition_strategy='mod')
print(mod.eval()) # output: [ 1, 10,  2, 20], p = id % len(params)

div = tf.nn.embedding_lookup([params1, params2], ids, partition_strategy='div')
print(div.eval()) # output: [ 1,  2, 10, 20], p = id / len(params)


#####################################################################################
# <codecell> 
#####################################################################################

params1 = tf.constant([1, 2, 3, 4])
params2 = tf.constant([10, 20, 30])
ids = tf.constant([[0, 1], [5, 2]])

mod = tf.nn.embedding_lookup([params1, params2], ids)
print(mod.eval())

div = tf.nn.embedding_lookup([params1, params2], ids, partition_strategy='div')
print(div.eval())


#####################################################################################
# <codecell> 
#####################################################################################

params1 = tf.constant([[1, 101], [2, 201], [3, 301], [4, 401]])
params2 = tf.constant([[10, 15], [20, 25], [30, 35]])
# ids = tf.constant([0, 1, 2, 3])
ids = tf.constant([[0, 1], [5, 2]])

mod = tf.nn.embedding_lookup([params1, params2], ids)
print(mod.eval())

div = tf.nn.embedding_lookup([params1, params2], ids, partition_strategy='div')
print(div.eval())
