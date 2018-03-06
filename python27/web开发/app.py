# -*- coding: UTF-8 -*-
import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>HOME</h1>'


@app.route('/signin', methods=['GET'])
def signin_from():
    return '''<form action="/signin" method="POST">
               <p style="color:red">测试登录页</p>            
               <p>用户 <input name="username"></p>
               <p>密码 <input name="password" type="password"></p>               
               <p><button name="submit">Sign in</button></p>
               </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容
    if flask.request.form['username'] == 'admin' and flask.request.form['password'] == 'password':
        return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run()
    # 运行python app.py，Flask自带的Server在端口5000上监听：
