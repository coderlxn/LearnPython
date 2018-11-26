# -*- coding: utf-8 -*-
# @Time    : 10/10/18 10:26 AM
# @Author  : Jax.Li
# @FileName: server.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

from flask import Flask, jsonify, abort, make_response, request, url_for
import time
from UNIT.jwusers import DepartmentDataUpdater
from UNIT.unit import request_unit

app = Flask(__name__)


@app.route("/api/v1.0/hello", methods=["GET"])
def hello():
    return jsonify({"result": "OK"})


# 初始化redis数据库中的部门和成员列表
@app.route("/api/v1.0/init", methods=["POST"])
def init():
    if "domain_id" not in request.json:
        return param_not_exists_error("domain_id")
    if "access_token" not in request.json:
        return param_not_exists_error("access_token")
    updater = DepartmentDataUpdater(request.json["domain_id"], request.json["access_token"])
    updater.start()
    return jsonify({"result": "Updating"})


@app.route("/api/v1.0/chat", methods=["POST"])
def message():
    if not request.json or "message" not in request.json:
        return param_not_exists_error("message")
    if not request.json or "access_token" not in request.json:
        return param_not_exists_error("access_token")
    bot_answer = request_unit(request.json["message"], request.json["access_token"])
    return jsonify({"message": bot_answer})


def param_not_exists_error(param):
    return jsonify({"message": param + "not exists"})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
