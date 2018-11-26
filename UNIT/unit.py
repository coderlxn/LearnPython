# -*- coding: utf-8 -*-
# @Time    : 10/8/18 11:30 AM
# @Author  : Jax.Li
# @FileName: unit.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import urllib
import json
from redis import Redis, RedisError
from datetime import datetime, timedelta
from UNIT.aifunctions import AIFunctions
from UNIT.jwhelper import redis
import base64

# client_id 为从UNIT的【发布上线】模块进入百度云创建应用后获取的API Key
client_id = 'haiIiyEAja8xcGGXWyTIC6Zt'
# client_secret 为从UNIT的【发布上线】模块进入百度云创建应用后获取的Secret Key
client_secret = 'o2NPtIze6pPgGgjweLVaRHOBSvMc6hCV'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
# 上面的XXXXXXX 要替换成自己的API Key，YYYYYY要换成自己的Secret Key

# 下面的log_id在真实应用中要自己生成，可是递增的数字
log_id = '7758523'
# 下面的user_id在真实应用中要是自己业务中的真实用户id、设备号、ip地址等，方便在日志分析中分析定位问题
user_id = '855654'
# 下面要替换成自己的bot_id
bot_id = '12699'

access_token = ""
bot_session = '""'


def create_unit_token():
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    global access_token
    access_token = json.load(response)["access_token"]
    # 将unit token写入redis
    redis.set("unit_access_token", access_token)
    dt = timedelta(days=10)
    redis.expire("unit_access_token", dt)
    print("UNIT token not exists, write to redis ", access_token)


def request_unit(query, jw_token):
    global access_token
    if redis.exists("unit_access_token"):
        access_token = str(redis.get("unit_access_token"))
        print("UNIT token exists, read from redis ", access_token)
    else:
        create_unit_token()

    global bot_session
    url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token
    post_data = '{\"bot_session\":' +bot_session +',\"log_id\":\"'+log_id+'\",\"request\":{\"bernard_level\":1,\"client_session\":\"{\\\"client_results\\\":\\\"\\\", \\\"candidate_options\\\":[]}\",\"query\":\"' + query + '\",\"query_info\":{\"asr_candidates\":[],\"source\":\"KEYBOARD\",\"type\":\"TEXT\"},\"updates\":\"\",\"user_id\":\"'+user_id+'\"},\"bot_id\":'+bot_id+',\"version\":\"2.0\"}'
    request = urllib.request.Request(url, post_data.encode('UTF-8'))

    request.add_header('Content-Type', 'application/json;charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        print(content)
    data = json.loads(content)
    print('用户问: ' + query)
    print('BOT答复: ' + data['result']['response']['action_list'][0]['say'])
    intent = data['result']['response']['schema']['intent']
    print('意图: ' + intent)
    bot_session = json.dumps(data["result"]["bot_session"])
    slots = data['result']['response']['schema']['slots']
    # print '词槽: ' + slot[0]['name'] + " = " +slot[0]['original_word']
    for slot in slots:
        print('词槽: ' + slot['name'] + " = " + slot['original_word'])

    # 使用AI来处理一次bot返回的数据
    ai = AIFunctions(jw_token)
    if len(slots) > 0 and hasattr(ai, intent.lower()):
        return getattr(ai, intent.lower())(slots)

    if intent == "" and len(slots) > 1:
        answer = data['result']['response']['action_list'][0]['say']
        for slot in slots:
            answer += "\n" + slot['original_word']
        return answer

    return data['result']['response']['action_list'][0]['say']


def download_department_list():
    if not redis.exists("department_by_name"):
        return
    names = redis.hkeys("department_by_name")
    with open("departments.txt", mode="wt", encoding="UTF-8") as f:
        for name in names:
            depart_name = base64.b64decode(name.decode("UTF-8")).decode("UTF-8")
            f.write(depart_name)
            f.write("\n")
            print(depart_name)


# download_department_list()
