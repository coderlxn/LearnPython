# -*- coding: utf-8 -*-
# @Time    : 11/20/18 3:43 PM
# @Author  : Jax.Li
# @FileName: threadeventdemo.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

from threading import Event, Thread
import time


def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)


started_evt = Event()

print('Launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()

started_evt.wait()
print("countdown is running")
