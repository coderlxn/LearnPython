# -*- coding: utf-8 -*-
# @Time    : 11/21/18 3:12 PM
# @Author  : Jax.Li
# @FileName: importer.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import importlib
from plugins import *


if __name__ == '__main__':
    module_bar = importlib.import_module("bar")
    module_bar.func()

    module_foo = importlib.import_module("foo")
    module_foo.func()
