# -*- coding: utf-8 -*-
# @Time    : 10/9/18 11:54 AM
# @Author  : Jax.Li
# @FileName: jwusers.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import urllib
import json
import threading
from UNIT.jwhelper import redis
import base64


class DepartmentDataUpdater(threading.Thread):
    def __init__(self, domain_id, token):
        threading.Thread.__init__(self)
        self.domain_id = domain_id
        self.token = token
        self.departments = [""]
        self.users = []

    def run(self):
        print("Start update department data")
        while len(self.departments) != 0:
            department_id = self.departments.pop()
            self.load_department_list(department_id)
        self.load_users_list()
        print("Update department data finished")

    def load_department_list(self, department_id):
        page_no = 0
        department_list = []  # 子部门id
        user_list = []  # 直属成员id
        while page_no >= 0:
            url = "https://www.joywok.com/api2/groups/deptusers?sort=name&pagesize=20&dept_id=%s&pageno=%d&domain_id" \
                  "=%s&access_token=%s" % (department_id, page_no, self.domain_id, self.token)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            content = response.read()
            jsonobj = json.loads(content)

            # 此处只处理部门列表，忽略用户列表，只有在部门列表超过一页时才加载下一页
            if jsonobj["JMStatus"]["code"] != 0:
                return
            if "users" in jsonobj["JMDepts"]:
                page_no = -1
            depts = jsonobj["JMDepts"]["depts"]
            # 将数据添加到Redis中
            for dept in depts:
                gid = dept["gid"]
                name = dept["name"]
                data = json.dumps(dept)
                redis.hmset("department_by_key", {gid: data})
                redis.hmset("department_by_name",
                            {base64.b64encode(bytes(name, encoding="UTF-8")).decode("UTF-8"): gid})
                # 将gid添加到待处理的部门列表中
                self.departments.append(gid)
                print("Add department %s to redis" % name)
                department_list.append(gid)
            users = jsonobj["JMDepts"]["users"]
            for user in users:
                uid = user["id"]
                user_list.append(uid)
        # 将子部门和直属成员列表添加到redis中
        print("department %s has %d department and %d members" % (department_id, len(department_list), len(user_list)))
        department_list = json.dumps(department_list)
        user_list = json.dumps(user_list)
        redis.hmset("department_list", {department_id: department_list})
        redis.hmset("user_list", {department_id: user_list})

    def load_users_list(self):
        url = "https://www.joywok.com/api2/users/objslist?domain_id=%s&access_token=%s" % (self.domain_id, self.token)
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            print(content)

        jsonobj = json.loads(content)
        if "JMObjs" in jsonobj:
            users = jsonobj["JMObjs"]["users"]
            for user in users:
                uid = user["id"]
                name = user["name"]
                # data = json.dumps(user)
                # objlist中的用户信息是不全的，此处添加空数据，在实际访问的时候再获取
                redis.hmset("user_by_key", {uid: ""})
                # TODO 处理同名的情况
                redis.hmset("user_by_name", {base64.b64encode(bytes(name, encoding="UTF-8")).decode("UTF-8"): uid})
                redis.hmset("user_by_name", {uid: name})
                # 处理名称中有别名的情况
                names = []
                if "(" in name:
                    names = name.split("(")
                elif "（" in name:
                    names = name.split("（")
                if len(names) > 1:
                    for name in names:
                        redis.hmset("user_by_name",
                                    {base64.b64encode(bytes(name.replace(")", "").replace("）", ""),
                                                            encoding="UTF-8")).decode("UTF-8"): uid})
                        print("Process alias ", name)
                print("Add user %s to redis" % name)
