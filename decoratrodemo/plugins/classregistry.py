# -*- coding: utf-8 -*-
# @Time    : 11/21/18 2:01 PM
# @Author  : Jax.Li
# @FileName: classregistry.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

REGISTERED_CLASSED = []


def registered_class(cls):
    REGISTERED_CLASSED.append(cls)
    print("Class {} registered".format(cls))
    return cls
