from app import create_app, db, cli
from app.models import User, Post
import os

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    deploy = int(os.environ.get("DEPLOYMENT") or 0)
    if 1 == deploy:
        app.run(host="0.0.0.0", debug=False, port=80)
    else:
        app.run(host="0.0.0.0", debug=True, port=5000)
