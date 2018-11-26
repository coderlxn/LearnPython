# -*- coding: utf-8 -*-
# @Time    : 10/11/18 4:26 PM
# @Author  : Jax.Li
# @FileName: aifunctions.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import json
import base64
from UNIT.jwhelper import redis, get_user_details
import datetime


class AIFunctions(object):
    def __init__(self, jw_token):
        self.jw_token = jw_token

    # 通过名称查询用户信息
    def user_info_basic(self, slots):
        if len(slots) == 0:
            return "相关词槽数据为空"

        for slot in slots:
            if slot['name'] == "user_user":
                user_name = slot["original_word"]
                name = base64.b64encode(bytes(user_name, encoding="UTF-8")).decode("UTF-8")
                print("check user by name ", name)
                if not redis.hexists("user_by_name", name):
                    return "%s 的相关信息不存在" % user_name
                uid = redis.hget("user_by_name", name).decode("UTF-8")
                data = get_user_details(uid, access_token=self.jw_token)
                obj = json.loads(data)
                user_info = "用户名：%s" % obj["name"]
                if "gender" in obj and obj["gender"] != "":
                    user_info += "\n性别：%s" % obj["gender"]
                if "birth" in obj and obj["birth"] != "":
                    user_info += "\n生日：%s" % obj["birth"]
                if "email" in obj and obj["email"] != "":
                    user_info += "\n邮箱：%s" % obj["email"]
                if "mobile" in obj:
                    user_info += "\n手机号：%s" % obj["mobile"]
                if "dept_name" in obj and obj["dept_name"] != "":
                    user_info += "\n部门：%s" % obj["dept_name"]
                if "title" in obj and obj["title"] != "":
                    user_info += "\n职位：%s" % obj["title"]
                return user_info
        return "相关词槽数据为空"

    def department_member_count(self, slots):
        if len(slots) == 0:
            return "相关词槽数据为空"

        for slot in slots:
            if slot['name'] == "user_deparment":
                name = slot["original_word"]
                department_name = base64.b64encode(bytes(name, encoding="UTF-8")).decode("UTF-8")
                if not redis.hexists("department_by_name", department_name):
                    return "%s 的相关信息不存在" % name
                uid = redis.hget("department_by_name", department_name).decode("UTF-8")
                # 查询部门直属成员人数
                if not redis.hexists("user_list", uid):
                    return "%s 的成员信息不存在" % name
                data = redis.hget("user_list", uid).decode("UTF-8")
                user_list = json.loads(data)
                return "%s 直属成员数目 %d" % (name, len(user_list))
        return "相关词槽数据为空"

    def department_members(self, slots):
        if len(slots) == 0:
            return "相关词槽数据为空"
        for slot in slots:
            if slot['name'] == "user_deparment":
                name = slot["original_word"]
                department_name = base64.b64encode(bytes(name, encoding="UTF-8")).decode("UTF-8")
                if not redis.hexists("department_by_name", department_name):
                    return "%s 的相关信息不存在" % name
                uid = redis.hget("department_by_name", department_name).decode("UTF-8")
                # 查询部门直属成员人数
                if not redis.hexists("user_list", uid):
                    return "%s 的成员信息不存在" % name
                data = redis.hget("user_list", uid).decode("UTF-8")
                user_list = json.loads(data)
                names = []
                for uid in user_list:
                    if redis.hexists("user_by_name", uid):
                        names.append(redis.hget("user_by_name", uid).decode("UTF-8"))
                    else:
                        names.append(uid)
                answer = "%s 直属成员列表：" % name
                for name in names:
                    answer += "\n%s" % name
                return answer
        return "相关词槽数据为空"

    def user_info_age(self, slots):
        if len(slots) == 0:
            return "相关词槽数据为空"

        for slot in slots:
            if slot['name'] == "user_user":
                user_name = slot["original_word"]
                name = base64.b64encode(bytes(user_name, encoding="UTF-8")).decode("UTF-8")
                print("check user by name ", name)
                if not redis.hexists("user_by_name", name):
                    return "%s 的相关信息不存在" % user_name
                uid = redis.hget("user_by_name", name).decode("UTF-8")
                data = get_user_details(uid, access_token=self.jw_token)
                obj = json.loads(data)
                if "birth" not in obj or obj["birth"] == "":
                    return "没有用户 %s 的生日相关信息" % user_name
                dt = obj["birth"]
                try:
                    dt = dt.replace(".", "/")
                    birthday = datetime.datetime.strptime(dt, '%Y/%m/%d')
                except ValueError:
                    return "生日格式错误 %s " % dt
                delta = datetime.datetime.now() - birthday
                years = int(delta.days / 365)
                return "%s 出生于 %s, 今年 %d 岁" % (obj["name"], dt, years)
        return "相关词槽数据为空"
