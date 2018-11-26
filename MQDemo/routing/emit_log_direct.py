# -*- coding: utf-8 -*-
# @Time    : 10/22/18 6:43 PM
# @Author  : Jax.Li
# @FileName: emit_log_direct.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="direct_logs",
                         exchange_type="direct")

severity = sys.argv[1] if len(sys.argv) > 2 else "info"
message = " ".join(sys.argv[2:]) or "Hello Routing!"
channel.basic_publish(exchange="direct_logs",
                      routing_key=severity,
                      body=message)
print("[x] Sent %r:%r" % (severity, message))
connection.close()
