# -*- coding: utf-8 -*-
# @Time    : 11/21/18 3:14 PM
# @Author  : Jax.Li
# @FileName: __init__.py.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import importlib


module_list = [importlib.import_module("importtest.plugins.plugina"), importlib.import_module("importtest.plugins.pluginb")]

__all__ = ["module_list"]
