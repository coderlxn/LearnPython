# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 11:43 AM
# @Author  : Jax.Li
# @FileName: lucusttest.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

from locust import HttpLocust, TaskSet, task


class TestLocalhost(TaskSet):
    @task
    def test_local(self):
        header = {"User-Agent": "Mozilla/5.0 "
                                "(Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                                "(KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}
        r = self.client.get("/", timeout=30, headers=header)
        assert r.status_code == 200


class WebsiteUser(HttpLocust):
    task_set = TestLocalhost

    min_wait = 3000
    max_wait = 6000
