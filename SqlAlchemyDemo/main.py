# -*- coding: utf-8 -*-
# @Time    : 2019-05-13 14:57
# @Author  : Jax.Li
# @FileName: main.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import os
from flask import Flask, render_template, request, flash, redirect
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_folder="static",template_folder="templates")

# 设置数据库连接属性
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# 实例化 ORM 操作对象
db = SQLAlchemy(app)

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('class_id', type=str)
parser.add_argument('class_name', type=str)
parser.add_argument('student_id', type=str)
parser.add_argument('student_name', type=str)


# 班级表
class Classes(db.Model):
    __tablename__ = "classes"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False,unique=True)
    # 一对多查询，从class通过relate_student指向student，从student通过relate_class指向class
    relate_student = db.relationship("Students", backref='relate_class', lazy='dynamic')


# 学生表
class Students(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40),nullable=False)
    cls_id = db.Column(db.Integer,db.ForeignKey("classes.id"))    # 注意要写成（表名.字段名）


class ClassesRestful(Resource):
    def get(self):
        args = parser.parse_args()
        class_id = args["class_id"]
        session = db.session
        return session.query(Classes).filter(Classes.id == class_id).first()


if __name__ == "__main__":
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5282)
