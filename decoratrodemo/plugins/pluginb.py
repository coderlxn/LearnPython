# -*- coding: utf-8 -*-
# @Time    : 11/21/18 2:19 PM
# @Author  : Jax.Li
# @FileName: pluginb.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

from .abstractplugin import AbstractPlugin
from .classregistry import registered_class


@registered_class
class PluginB(AbstractPlugin):
    def __init__(self):
        print("Plugin B init")

    def attack(self):
        print("Plugin B attacting")
