# -*- coding: utf-8 -*-
# @Time    : 10/12/18 10:17 AM
# @Author  : Jax.Li
# @FileName: jwhelper.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

from redis import Redis
import urllib
import json

redis = Redis(host="140.143.18.162", db=0, socket_connect_timeout=2, socket_timeout=2, password="runoob")


def get_user_details(user_id, access_token):
    # 如果redis中有指定数据，则从redis读取
    if redis.hexists("user_by_key", user_id) and redis.hget("user_by_key", user_id).decode("UTF-8") != "":
        return redis.hget("user_by_key", user_id).decode("UTF-8")

    url = "https://www.joywok.com/api2/users/userinfo?access_token=%s&id=%s" % (access_token, user_id)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    content = response.read()
    obj = json.loads(content)
    obj = obj["JMUserDetail"]
    content = json.dumps(obj)
    # 将用户信息写入redis数据库中
    redis.hset("user_by_key", user_id, content)
    return content
