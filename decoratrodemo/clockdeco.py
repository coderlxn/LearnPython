# -*- coding: utf-8 -*-
# @Time    : 11/16/18 5:20 PM
# @Author  : Jax.Li
# @FileName: clockdeco.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(", ".join(repr(arg) for arg in args))
        if kwargs:
            pairs = ["%s=%r" % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(", ".join(pairs))
        arg_str = ", ".join(arg_lst)
        print("[%0.8fs] %s(%s) -> %r " % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@functools.lru_cache()
@clock
def fibonacci_ex(n):
    if n < 2:
        return n
    return fibonacci_ex(n - 2) + fibonacci_ex(n - 1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
    print('*' * 40, 'Calling fibonacci(6)')
    print(fibonacci(6))
    print('*' * 40, 'Calling fibonacci_ex(6)')
    print(fibonacci_ex(6))
