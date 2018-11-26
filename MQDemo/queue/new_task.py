# -*- coding: utf-8 -*-
# @Time    : 10/22/18 10:37 AM
# @Author  : Jax.Li
# @FileName: new_task.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import sys
import pika

messages = " ".join(sys.argv[1:]) or "Hello MQ queue........."
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)  # 持久化

for i in range(10):
    channel.basic_publish(exchange="",
                          routing_key="task_queue",
                          body=messages,
                          properties=pika.BasicProperties(
                            delivery_mode=2,  # make message persistent
                          ))
print(messages)
connection.close()
