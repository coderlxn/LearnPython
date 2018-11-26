# -*- coding: utf-8 -*-
# @Time    : 11/21/18 1:59 PM
# @Author  : Jax.Li
# @FileName: pluginsystem.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

from decoratrodemo.plugins import *
for cls in REGISTERED_CLASSED:
    item = cls()
    item.attack()
