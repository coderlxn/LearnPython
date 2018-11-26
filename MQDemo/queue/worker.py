# -*- coding: utf-8 -*-
# @Time    : 10/22/18 10:53 AM
# @Author  : Jax.Li
# @FileName: worker.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import pika
import time


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)
    time.sleep(body.count(b"."))
    print("[x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="task_queue", durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue="task_queue")
print("[*] Waiting for messages. To exit press CTRL+C")
while True:
    try:
        channel.start_consuming()
        print("After start consuming")
    except pika.exceptions.ConnectionClosed:
        continue
