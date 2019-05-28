#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @file introduction.py
# @brief
# @author QRS
# @blog qrsforever.github.io
# @version 1.0
# @date 2019-05-28 18:32:34

import tensorflow as tf


#####################################################################################
# <codecell> tensor values
#####################################################################################

a = tf.constant([1., 2., 3.])
a.get_shape() # TensorShape([Dimension(3)])
a._rank() # 1

b = tf.constant([[1., 2.], [3., 4.]])
b.get_shape() # TensorShape([Dimension(2), Dimension(2)])
b._rank() # 2

c = tf.constant([[[1., 2., 3.]], [[4., 5., 6.]]])
c.get_shape() # TensorShape([Dimension(2), Dimension(1), Dimension(3)])
c._rank() # 3
print(c) # Tensor("Const_8:0", shape=(2, 1, 3), dtype=float32)

# **tf.Tensors don't have values, just handles to elements in graph.**

#####################################################################################
# <codecell> Graph just like a program (static)
#####################################################################################

# Graph <-- tf.Operation(node) + tf.Tensors(edges)

a = tf.constant(3.0, dtype=tf.float32)
b = tf.constant(4.0)
total = a + b # + is a tf.Operation
print(a, total) # Tensor


#####################################################################################
# <codecell> TensorBoard
#####################################################################################

writer = tf.summary.FileWriter("/tmp/tf")
writer.add_graph(tf.get_default_graph())
writer.flush()

#####################################################################################
# <codecell> Session
#####################################################################################

sess = tf.Session()
print(sess.run(a)) # 3.0
print(sess.run(a)) # 3.0 becase it is constant tensor
print(sess.run(total)) # 7.0

print(sess.run({'ab':(a,b), 'total':total})) # {'ab': (3.0, 4.0), 'total': 7.0}

vec = tf.random_uniform(shape=(3,), dtype=tf.float32)
out1 = vec + 1
out2 = vec + 2

print(sess.run(vec)) # [0.48206675 0.28447366 0.6557442 ]
print(sess.run(vec)) # [0.71749437 0.3975991  0.18789124] diff twice
print(sess.run((out1, out2)))


#####################################################################################
# <codecell> placeholder
#####################################################################################

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

z = x + y

print(sess.run(z, feed_dict={x: 3, y: 4})) # 7.0
print(sess.run(z, feed_dict={x: [3, 3], y: [4, 4]})) # [7. 7.]

#####################################################################################
# <codecell> Dataset, yet placeholder only for simple experiments
#####################################################################################

data = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]
slices = tf.data.Dataset.from_tensor_slices(data) # DatasetV1Adapter
next_item = slices.make_one_shot_iterator().get_next() # Tensor

print(sess.run(next_item)) # [1 2]

while True:
    try:
        print(sess.run(next_item))
        # [3 4]
        # [5 6]
        # [7 8]
    except tf.errors.OutOfRangeError:
        break # end

# if dataset depends on statefull operation, use below

data = tf.random_normal((6, 3))
slices = tf.data.Dataset.from_tensor_slices(data)
iterator = slices.make_initializable_iterator()
next_item = iterator.get_next()

sess.run(iterator.initializer)

print(sess.run(next_item)) # [ 1.1039894  -0.01763356  0.69782484]

while True:
    try:
        print(sess.run(next_item))
        # [ 1.7729928  -0.47896445 -0.21015473]
        # [ 1.1517383  -1.5633205  -0.56522846]
        # [-0.1289624   0.78403634  0.28383535]
        # [-0.9788238  -0.3450247  -1.5973071]
        # [ 0.7695466  -0.00325457 -1.5413337 ]
    except tf.errors.OutOfRangeError:
        break # end


#####################################################################################
# <codecell> Layer (*?*)
#####################################################################################

x = tf.placeholder(tf.float32, shape=(None, 3))
layer = tf.keras.layers.Dense(units=1)
y = layer(x)

init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(y, {x:[[1,2,3], [4,5,6]]}))
# [[-4.433628]
# [-9.467066]]

#####################################################################################
# <codecell> Feature column (将不是数字的格式转换为数字 (媒介)
#####################################################################################

