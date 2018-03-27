TensorFlow
==========

Install
-------

1. sudo pip3 install tensorflow
2. sudo pip3 install tensorflow-gpu

如果上面步骤失败:

` sudo pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.1.0-cp34-cp34m-linux_x86_64.whl `

Test
----

```python
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
```

```html
<pre>...</pre>
```

```cpp
int main(int, char**)
{

}
```
