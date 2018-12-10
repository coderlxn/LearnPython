# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 7:54 PM
# @Author  : Jax.Li
# @FileName: loggenerator.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com


import faker
import datetime
import time
import random
import uuid
import json

client = ["xmppclient", "processer", "queryer", "callback", "audioconverter"]
# level = ["debug", "info", "warning", "error"]

if __name__ == '__main__':
        faker = faker.Faker()
        uid = str(uuid.uuid4())
        while True:
        # for index in range(10):
            if random.randrange(0, 2) == 0:
                uid = str(uuid.uuid4())
            lv = random.randint(1, 10)
            if lv <= 4:
                level = "debug"
            elif lv <= 8:
                level = "info"
            elif lv <= 9:
                level = "warning"
            else:
                level = "error"

            log_item = {"@timestamp": str(datetime.datetime.utcnow() + datetime.timedelta(hours=8)),
                        "message": faker.sentence(nb_words=9), "muid": uid, "level": level}
            log = json.dumps(log_item)
            print(log)

            fl = random.randint(1, 4)
            if fl == 1:
                filename = "/usr/log/xmppclient-a79874f161b7.log"
            elif fl == 2:
                filename = "/usr/log/querier-a79874f161b7.log"
            elif fl == 3:
                filename = "/usr/log/callback-a79874f161b7.log"
            else:
                filename = "/usr/log/processor-a79874f161b7.log"
            with open(filename, "a") as file:
                file.write(log)
                file.write("\n")
            time.sleep(2)
