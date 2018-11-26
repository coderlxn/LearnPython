# -*- coding: utf-8 -*-
# @Time    : 9/28/18 7:32 PM
# @Author  : Jax.Li
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com


import os
import time

from plugin import loader

p = loader.Loader('/tmp')

while True:
    os.system("wget -q -r -np -nH --reject='index.html*,*.pyc' -P %s 'http://127.0.0.1:8080'" % p.plugin_dir)

    ok, m = p.load_plugin('pluginA')
    if ok:
        getattr(m, 'f')()
    else:
        print('no such plugin pluginA')

    ok, m = p.load_plugin('pluginB')
    if ok:
        getattr(m, 'f')()
    else:
        print('no such plugin pluginB')

    ok, m = p.load_plugin('pluginC')
    if ok:
        getattr(m, 'f')()
    else:
        print('no such plugin pluginC')

    ok, m = p.load_plugin('pluginD')
    if ok:
        getattr(m, 'f')()
    else:
        print('no such plugin pluginD')
