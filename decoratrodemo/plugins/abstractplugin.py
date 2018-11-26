# -*- coding: utf-8 -*-
# @Time    : 11/21/18 2:07 PM
# @Author  : Jax.Li
# @FileName: abstractplugin.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com


class AbstractPlugin(object):
    def __init__(self):
        print("Abstract Plugin init")

    def attack(self):
        print("attacting")
