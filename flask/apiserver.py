# -*- coding: utf-8 -*-
# @Time    : 10/10/18 5:01 PM
# @Author  : Jax.Li
# @FileName: apiserver.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

from flask import Flask, jsonify, abort, make_response, request, url_for
import time

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
        "done": False,
    },
    {
        "id": 2,
        "title": "Learn Python",
        "description": "Need to find a good Python tutorial on the web",
        "done": False,
    },
]


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == "id":
            new_task["uri"] = url_for("get_task", task_id=task["id"], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


@app.route('/test/completor', methods=['GET'])
def test_completor():
    return jsonify({'hello': 'completor'})


@app.route("/todo/api/v1.0/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": list(map(make_public_task, tasks))})


@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = list(filter(lambda t: t["id"] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify({"task": task[0]})


@app.route("/todo/api/v1.0/tasks", methods=["POST"])
def create_task():
    if not request.json or "title" not in request.json:
        abort(404)

    task = {
        "id": tasks[-1]["id"] + 1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False
    }
    tasks.append(task)
    return jsonify({"task": task}), 201


@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = list(filter(lambda t: t["id"] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if "done" in request.json and not isinstance(request.json["done"], bool):
        abort(400)
    task[0]["title"] = request.json.get("title", task[0]["title"])
    task[0]["description"] = request.json.get("description", task[0]["description"])
    task[0]["done"] = request.json.get("done", task[0]["done"])
    return jsonify({"task": task[0]})


@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = list(filter(lambda t: t["id"] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({"result": True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    app.run(debug=True)
