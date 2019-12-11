import click
from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from src import adb


def get_db():
    return adb


def close_db(e=None):
    pass
    # db = g.pop('db', None)
    
    # if db is not None:
    #     db.close()
        
        
def init_db():
    db = get_db()
    db.create_all()
    

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    print('init db app')


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database')