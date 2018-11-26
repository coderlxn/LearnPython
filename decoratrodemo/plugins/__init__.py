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

__all__ = ["REGISTERED_CLASSED"]
