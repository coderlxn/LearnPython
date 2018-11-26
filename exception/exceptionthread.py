# -*- coding: utf-8 -*-
# @Time    : 11/22/18 5:05 PM
# @Author  : Jax.Li
# @FileName: exceptionthread.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import sys
import time
import traceback
from threading import Thread


class CountDown(Thread):
    def __init__(self):
        super(CountDown, self).__init__()
        self.exitcode = 0
        self.exception = None
        self.exc_traceback = ''

    def run(self):
        try:
            self._run()
        except Exception as what:
            self.exitcode = 1
            self.exception = what
            self.exc_traceback = ''.join(traceback.format_exception(*sys.exc_info()))

    def _run(self):
        num = 100
        print('slave start')
        for i in range(5, -1, -1):
            print('Num: {0}'.format(num/i))
            time.sleep(1)
        print('slave end')


if __name__ == '__main__':
    print('main start')
    td = CountDown()
    td.start()
    td.join()
    if td.exitcode != 0:
        print("Exception in {} catch by main".format(td.getName()))
        print(td.exc_traceback)
    print('main end')
