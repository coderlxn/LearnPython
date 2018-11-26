# -*- coding: utf-8 -*-
# @Time    : 11/20/18 2:10 PM
# @Author  : Jax.Li
# @FileName: testimportall.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com


def spam():
    pass


def grok():
    pass


blah = 42
# __all__ = ['spam', 'grok'] 如果定义了__all__，在from xxx import * 时，只有在__all__中的对象会被导入
