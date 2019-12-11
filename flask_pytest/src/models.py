from flask_sqlalchemy import SQLAlchemy
from src.db import get_db

db = get_db()

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), index=True)
    password = db.Column(db.String(256), index=True)