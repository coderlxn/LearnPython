# -*- coding: utf-8 -*-
# @Time    : 10/11/18 11:35 AM
# @Author  : Jax.Li
# @FileName: threadingdemo.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print("Exiting " + self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            threading.current_thread().exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)


thread1.start()
thread2.start()


print("Exiting Main Thread")
