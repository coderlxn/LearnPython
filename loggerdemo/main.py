# -*- coding: utf-8 -*-
# @Time    : 10/18/18 6:05 PM
# @Author  : Jax.Li
# @FileName: main.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import logging
import time
import random
from loggerdemo.SafeFileHandler import SafeFileHandler

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        handlers=[SafeFileHandler("my.log", mode="a", encoding="UTF-8")])

    key_id = random.randint(1, 100)
    while True:
        logging.info("Test logging %d %f " % (key_id, time.time()))
        time.sleep(1)
