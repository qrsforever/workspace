#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file ch04.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-27 13:22:40

#############################  jupyter-vim map ######################################
# https://github.com/qrsforever/vim/blob/master/bundle/.configs/jupyter-vim_conf.vim
#   ,ji: import file; ,je: run cell; ,jj: run current line
#   ,jc: clear buffer; ju: update buffer; jq: quit buffer
#   ,jh: open buffer horizontally; jv: open buffer virtually
#   ,jp: print <cword> variable; ,jt: print <cword> type
#   ,j1: output <cword> head(1), j2, j3, j4, j5 is also
#   ,j6: output <cword> tail(1), j7, j8, j9, j0 is also
#####################################################################################

import tensorflow as tf

#####################################################################################
# <codecell> 训练和评估的基本代码框架
#####################################################################################

#     输入数据       执行推断模型    计算损失    调整模型参数
#  -----> inputs ----> inference ----> loss -----> train
#    ^                                              |
#    |                                              |
#    +----------------------------------------------+
# 
#    evaluate 评估

#####################################################################################
# <codecell> 4.3 线性回归
#####################################################################################

W = tf.Variable(tf.zeros([2,1]), name='weight')
b = tf.Variable(0.0, name='bias')

def inputs():
    X = [[84, 46], [73, 20], [65, 52], [70, 30], [76, 57], [69, 25],
            [63, 28], [72, 36], [79, 57], [75, 44], [27, 24], [89, 31], [65, 52],
            [57, 23], [59, 60], [69, 48], [60, 34], [79, 51], [75, 50], [82, 34],
            [59, 46], [67, 23], [85, 37], [55, 40], [63, 30]]
    Y = [354, 190, 405, 263, 451, 302, 288, 385, 402, 365, 209,
            290, 346, 254, 395, 434, 220, 374, 308, 220, 311, 181, 274, 303, 244]
    return tf.cast(X, tf.float32),  tf.cast(Y, tf.float32)

def inference(X):
    return tf.matmul(X, W) + b

def loss(X, Y):
    Y_predicted = inference(X)
    return tf.reduce_sum(tf.squared_difference(Y, Y_predicted))

def train(loss):
    learning_rate = 0.000001
    return tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess:

    X, Y = inputs()
    # X, Y: <class 'tensorflow.python.framework.ops.Tensor'>
    s_loss = loss(X, Y)
    # s_loss: <class 'tensorflow.python.framework.ops.Tensor'>
    tr_op = train(s_loss)
    # tr: <class 'tensorflow.python.framework.ops.Operation'>
    steps = 10000
    for step in range(steps):
        sess.run([tr_op])
        if step % 1000 == 0:
            print("Epoch:", step, " loss: ", sess.run(s_loss))

