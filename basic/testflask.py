from flask import Flask
from flask import render_template
from flask import request, abort, redirect, url_for
from werkzeug import security

app = Flask(__name__)


@app.route('/')
def index():
    # return 'Index Page'
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)


@app.route('/helloworld')
def helloworld():
    return 'Hello World!'


# 在URL中指定参数
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


# # get和post
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # error = None
#     # if request.method == 'POST':
#     #     if valid_login(request.form['username'], request.form['password']):
#     #         return log_
#     pass


# 加载模板，render_template会自动去templates目录下寻找模板文件，静态文件在static目录下
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# 上传文件
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    print("upload file")
    if request.method == 'POST':
        f = request.files['the_file']
        f.save(f.filename)


with app.test_request_context('hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'


if __name__ == '__main__':
    app.run(debug=True)
