# -*- coding: utf-8 -*-
# @Time    : 11/14/18 7:31 PM
# @Author  : Jax.Li
# @FileName: registration.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


if __name__ == '__main__':
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()
