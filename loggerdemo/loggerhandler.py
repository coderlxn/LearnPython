# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 5:57 PM
# @Author  : Jax.Li
# @FileName: loggerhandler.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import logging
import uuid

service_id = str(uuid.uuid4())[-12:]
logger = logging.FileHandler('debug-{}.log'.format(service_id))
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("info-{}.log".format(service_id))
fh.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setFormatter(formatter)

logging.basicConfig(level=logging.DEBUG,
                    handlers=[logger, fh])

logging.info("hello")
logging.debug("debug lines")
logging.error("wow! error occurred")
