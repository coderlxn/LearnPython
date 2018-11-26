# -*- coding: utf-8 -*-
# @Time    : 11/19/18 10:05 AM
# @Author  : Jax.Li
# @FileName: exceptiondemo.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

# try:
#     msg = input(">> ")
#     print(int(msg))
# except Exception as e:
#     print("异常的类型是:%s" % type(e))
#     print("异常的内容是:%s" % e)
# else:
#     print("代码库不抛出异常会执行此行代码")
# finally:
#     print("始终会执行的代码")

msg = input(">> ")
print(int(msg))

print("后续的代码")
