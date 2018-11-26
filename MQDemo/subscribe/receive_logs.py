# -*- coding: utf-8 -*-
# @Time    : 10/22/18 6:03 PM
# @Author  : Jax.Li
# @FileName: receive_logs.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="logs",
                         exchange_type="fanout")

result = channel.queue_declare(exclusive=True)  # 退出时删除channel
queue_name = result.method.queue

channel.queue_bind(exchange="logs",
                   queue=queue_name)

print("[*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print("[*] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
