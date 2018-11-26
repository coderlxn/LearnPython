# -*- coding: utf-8 -*-
# @Time    : 11/2/18 2:42 PM
# @Author  : Jax.Li
# @FileName: basictest.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import tensorflow as tf

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])

product = tf.matmul(matrix1, matrix2)

with tf.Session() as sess:
    result = sess.run(product)
    print(result)
