# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 3:19 PM
# @Author  : Jax.Li
# @FileName: loggenerater.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import faker
import datetime
import time

if __name__ == '__main__':
    faker = faker.Faker()
    # while True:
    for index in range(10):
        log = "{}    INFO    {}\n".format(str(datetime.datetime.now()), faker.sentence(nb_words=9))
        print(log)
        time.sleep(2)
        with open("/usr/log/python.log", "a") as file:
            file.write(log)
