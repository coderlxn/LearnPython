# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 17:42
# @Author  : Jax.Li
# @FileName: sleepwait.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import requests
import json
import time
import logging

token = ''
while token == '':
    password = 'a123456'
    email = 'lxn5@iphoto55.hk'
    url = "https://www.joywok.com/api2/account/login?appkey=joywok_robot&appsecret=ploLEtJUYdjdH3zK&devicePlatform=robot" \
          "&password=%s&email=%s" % (password, email)
    # req = requests.Request(url=url, data=body.encode('UTF-8'),
    #                        headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
    print("getting token")
    try:
        response = requests.get(url)
        content = response.content
        obj = json.loads(content)
    except Exception as e:
        print(repr(e))
    else:
        token = obj["JMStatus"]["access_token"]
        uid = obj["JMUser"]["id"]

    if token == '':
        print('token is still empty try again later')
        time.sleep(10)
print(token)
