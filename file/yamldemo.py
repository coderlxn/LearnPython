# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 6:14 PM
# @Author  : Jax.Li
# @FileName: yamldemo.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import yaml

with open("demo.yml", "rt") as f:
    text = f.read()
    obj = yaml.load(text)
    print(obj)
