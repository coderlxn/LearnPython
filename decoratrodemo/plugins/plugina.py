# -*- coding: utf-8 -*-
# @Time    : 11/21/18 2:03 PM
# @Author  : Jax.Li
# @FileName: plugina.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

from .abstractplugin import AbstractPlugin
from .classregistry import registered_class

print("plugina imported")


@registered_class
class PluginA(AbstractPlugin):
    def __init__(self):
        print("Plugin A init")

    def attack(self):
        print("Plugin A attacting")
