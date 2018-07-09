from flask import Flask
# from app import views
# from app import app

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "Hello, Flask Demo!"


if __name__ == '__main__':
    app.run(debug=True)
