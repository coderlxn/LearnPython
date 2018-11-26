# -*- coding: utf-8 -*-
# @Time    : 11/20/18 11:33 AM
# @Author  : Jax.Li
# @FileName: printurl.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com


def url_print(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    return url
