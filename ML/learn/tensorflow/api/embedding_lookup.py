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
# <codecell> 多Tensor, 每个tensor第一维包含的元素个数相同(其他维度shape必须相同)
#####################################################################################

sess = tf.InteractiveSession()

param1 = tf.constant([[1, 101], [2, 102], [3, 103], [33, 333]])
param2 = tf.constant([[4, 104], [5, 105], [6, 106], [66, 666]])
param3 = tf.constant([[7, 107], [8, 108], [9, 109], [99, 999]])

params = [param1, param2, param3]
ids = tf.constant([0, 1, 2, 3, 4, 7])

#
# 分析:
#   第一个关键数字是"3": params由3个tensor组成, ids索引分别从这个3个分区选取
#   第二个关键数字是"12": 12 = 3(tensor个数) x 4(每个tensor的第一维个数), 即最大id+1
#   第三个关键数字是"4": 4 = (11 + 1) / 3 (得出每个tensor应该含有id的最大个数)
#                        11是ids中最大下标 = 所有tensor第一维元素个数总和
#
#   "mod": id % 3 代表落入哪个tensor中, eg: 7 % 3 = 1(第二个tensor中)
#       tensor0包含的ids: [ 0, 3, 6, 9 ]
#       tensor1包含的ids: [ 1, 4, 7, 10 ]
#       tensor2包含的ids: [ 2, 5, 8, 11 ]
#
#                      [1, 101]  [2, 102]  [3, 103]  [33, 333]
#                         0         3         6          9
#                      [4, 104]  [5, 105]  [6, 106]  [66, 666]
#                         1         4         7         10
#                      [7, 107]  [8, 108]  [9, 109]  [99, 999]
#                         2         5         8         11
#
#   "div": id // 4 代表落入哪个tensor中, eg: 7 // 4 = 1(第二个tensor中)
#       tensor0包含的ids: [ 0, 1, 2, 3 ]
#       tensor1包含的ids: [ 4, 5, 6, 7 ]
#       tensor2包含的ids: [ 8, 9, 10, 11 ]
#
#                      [1, 101]  [2, 102]  [3, 103]  [33, 333]
#                         0         1         2          3
#                      [4, 104]  [5, 105]  [6, 106]  [66, 666]
#                         4         5         6          7
#                      [7, 107]  [8, 108]  [9, 109]  [99, 999]
#                         8         9        10         11

mod = tf.nn.embedding_lookup(params, ids)
print(mod.eval())

# [[  1 101]
#  [  4 104]
#  [  7 107]
#  [  2 102]
#  [  5 105]
#  [  6 105]]

div = tf.nn.embedding_lookup(params, ids, partition_strategy='div')
print(div.eval())

# [[  1 101]
#  [  2 102]
#  [  3 103]
#  [ 33 333]
#  [  4 104]
#  [ 66 666]]

#

sess.close()

#####################################################################################
# <codecell> 多Tensor, 每个tensor第一维包含的元素个数不同(其他维度shape必须相同)
#####################################################################################

sess = tf.InteractiveSession()

param1 = tf.constant([[1, 101], [2, 102], [3, 103], [4, 104], [33, 333]])
param2 = tf.constant([[5, 105], [6, 106]])
param3 = tf.constant([[7, 107], [8, 108], [9, 109], [99, 999]])

params = [param1, param2, param3]
ids = tf.constant([0, 1, 2, 3, 4, 5, 8])


# 分析:
#     3个tensor
#     11个元素: 9 = 5 + 2 + 4
#     每个tensor含有的id的最大个数 4 = (11 + 1) / 3
#
#     "mod":
#       tensor0包含的ids: [ 0, 3, 6, 9 ]
#       tensor1包含的ids: [ 1, 4, 7, 10 ]
#       tensor2包含的ids: [ 2, 5, 8, 11 ]
#
#                    [1, 101]  [2, 102]  [3, 103], [4, 104], [33, 333]
#                       0         3         6         9
#                    [5, 105]  [6, 106]    ---       ---
#                       1         4         7         10
#                    [7, 107]  [8, 108], [9, 109], [9, 999]
#                       2         5         8         11
#      注意: 如果ids中含有7 || 10, 将会报错, 该位置是空
#
#      "div":
#       tensor0包含的ids: [ 0, 1, 2, 3 ]
#       tensor1包含的ids: [ 4, 5, 6, 7 ]
#       tensor2包含的ids: [ 8, 9, 10, 11 ]
#
#                    [1, 101]  [2, 102]  [3, 103], [4, 104], [33, 333]
#                       0         1         2         3
#                    [5, 105]  [6, 106]    ---       ---
#                       4         5         6         7
#                    [7, 107]  [8, 108], [9, 109], [99, 999]
#                       8         9         10        11
#       注意: 如果ids中含有 6 || 7, 将会报错, 该位置是空

mod = tf.nn.embedding_lookup(params, ids)
print(mod.eval())

# [[  1 101]
#  [  5 105]
#  [  7 107]
#  [  2 102]
#  [  6 106]
#  [  8 108]
#  [  9 109]]

div = tf.nn.embedding_lookup(params, ids, partition_strategy='div')
print(div.eval())

# [[  1 101]
#  [  2 102]
#  [  3 103]
#  [  4 104]
#  [  5 105]
#  [  6 106]
#  [  7 107]]

ids = tf.constant([7])

try:
    mod = tf.nn.embedding_lookup(params, ids)
    print(mod.eval())
except: # noqa: E722
    print("indices[0] = 2 is not in [0, 2)")

try:
    div = tf.nn.embedding_lookup(params, ids, partition_strategy='div')
    print(div.eval())
except: # noqa: E722
    print("indices[0] = 3 is not in [0, 2)")

sess.close()
