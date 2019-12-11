from src.models import UserModel
from src.db import get_db
from flask_restful import Resource, abort, request
from flask_babel import gettext as _

class Auth(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        session = get_db().session
        user = session.query(UserModel).filter(UserModel.username == username).first()
        if user is not None:
            abort(400, message=_('{} already exists!'))
        session.add(UserModel(username=username, password=password))
        session.commit()
        
        return 'success', 201
        
    
        