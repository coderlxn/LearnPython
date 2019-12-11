import os
from flask import Flask, g ,request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel


adb = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite',
        SQLALCHEMY_COMMIT_ON_TEARDOWN = True,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    adb.init_app(app)
    
    babel = Babel(app)
    
    LANGUAGES = {
        "zh": "Chinese",  # 中文
        "en": "English"  # 英文
    }


    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(LANGUAGES.keys())
    

    @babel.timezoneselector
    def get_timezone():
        user = getattr(g, 'user', None)
        if user is not None:
            return user.timezone
    
    from . import db as rdb
    rdb.init_app(app)
    
    api = Api(app)
    from . import auth
    api.add_resource(auth.Auth, '/api/v1/auth')

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app