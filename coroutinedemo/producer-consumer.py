# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 10:22 AM
# @Author  : Jax.Li
# @FileName: producer-consumer.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import time


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print("[CONSUMER] Consuming %s..." % n)
        time.sleep(1)
        r = "200 OK"


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("[PRODUCER] Producing %s..." % n)
        r = c.send(n)
        print("[PRODUCER] Consumer return: %s" % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    producer(c)
