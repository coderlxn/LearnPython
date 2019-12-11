import os
import tempfile

import pytest
from src import create_app
from src.db import get_db, init_db

@pytest.fixture
def app():
    
    db_fd, db_path = tempfile.mkstemp()
    
    app = create_app(test_config={'SQLALCHEMY_DATABASE_URI': 'sqlite:///{}'.format(db_path)})
    with app.app_context():
        db = get_db()
        init_db()
        
    yield app
    
    os.close(db_fd)
    os.unlink(db_path)
    

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()