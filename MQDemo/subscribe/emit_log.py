# -*- coding: utf-8 -*-
# @Time    : 10/22/18 5:59 PM
# @Author  : Jax.Li
# @FileName: emit_log.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import pika
import sys
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="logs",
                         exchange_type="fanout")

for i in range(10):
    message = " ".join(sys.argv[1:]) or "info: Hello Subscribe %d!" % random.randint(0, 1000)
    channel.basic_publish(exchange="logs",
                          routing_key="",
                          body=message)
    print("[x] Sent %r" % message)
connection.close()
