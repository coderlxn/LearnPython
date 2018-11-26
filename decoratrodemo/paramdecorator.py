# -*- coding: utf-8 -*-
# @Time    : 11/20/18 6:28 PM
# @Author  : Jax.Li
# @FileName: paramdecorator.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

registry = set()


# 实际是调用一个工厂函数来返回一个装饰器
def register(active=True):
    def decorate(func):
        print("running register(active=%s)->decorate(%s)" % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate


@register(active=False)
def f1():
    print("running f1()")


@register()
def f2():
    print("running f2()")


def f3():
    print("running f3()")


f1()
f2()
f3()
