# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 9:15 AM
# @Author  : Jax.Li
# @FileName: testdocker.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import os
import socket
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return "This is the index page"


@app.route("/hello")
def hello():
    return jsonify("hello")


@app.route("/info")
def info():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return "machine ip address: {}".format(ip)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route("/exit")
def exit_service():
    os._exit(0)
    # shutdown_server()
    return jsonify("shutting down")


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    except RuntimeError as msg:
        print(msg)
