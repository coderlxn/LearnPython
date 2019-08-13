# -*- coding: utf-8 -*-
# @Time    : 2019-07-08 10:16
# @Author  : Jax.Li
# @FileName: file_read_and_write.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

from faker import Faker

fk = Faker('zh_CN')

with open("username_lookup.txt", 'w') as fw:
    for i in range(1024):
        fw.write("{}\n".format(fk.department()))

with open('username_lookup.txt') as fr:
    while True:
        try:
            text = fr.readline()
        except Exception as e:
            print(e)
        if text == "":
            break
        print(text, end='')
