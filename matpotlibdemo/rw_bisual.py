# -*- coding: utf-8 -*-
# @Time    : 10/17/18 6:07 PM
# @Author  : Jax.Li
# @FileName: rw_bisual.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import matplotlib.pylab as plt
from matpotlibdemo.random_walk import RandomWalk


while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.figure()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors="none", s=1)

    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("是否继续生成？")
    if keep_running == "n":
        break