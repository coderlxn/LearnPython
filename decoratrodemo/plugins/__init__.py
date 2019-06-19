# -*- coding: utf-8 -*-
# @Time    : 11/21/18 2:00 PM
# @Author  : Jax.Li
# @FileName: __init__.py.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import importlib
from .classregistry import REGISTERED_CLASSED
from os.path import basename, dirname, join
from glob import glob

pwd = dirname(__file__)
lst = glob(join(pwd, "*.py"))
for x in lst:
    file_name = basename(x)
    if not file_name.startswith("__"):
        importlib.import_module(".{}".format(file_name[:-3]), __package__)

# 它是一个string元素组成的list变量，定义了当你使用 from <module> import * 导入某个模块的时候能导出的符号（这里代表变量，函数，类等）。
__all__ = ["REGISTERED_CLASSED"]
