# -*- coding: UTF-8 -*-
# 了解来WSGI框架，我们发现，其实一个WEB AP，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应
# 但是如何处理HTTP请求不是问题，问题是如何处理100个不同的URL
# 每一个URL可以对GET和POST全in 个球，当然还有PUT、DELETE等请求，但是我们通常指考虑最常见的GET和POST请求
# 一个最简单的想法是从environ变量去除HTTP请求的信息，然后逐一判断：
# def application(environ,start_response):
#     method=environ['REQUEST_METHOD']
#     path=environ['PATH_INFO']
#     if method=='GET' and path=='/':
#         return handle_home(environ,start_response)
#     if method=='POST' and path=='/sgnin':
#         return handle_signin(environ,start_response)
#     ...
# 指示这么写下去代码是肯定没法维护了
# 代码这么写没法维护的原因是因为WSGI提供的接口虽然比HTTP接口高级了不少，但是和WEB APP的处理逻辑比，还是比较低级，我们需要在WSGI接口之上进一
# 步的抽象，让我们专注于用一个函数处理一个URL ，至于URL到函数的映射，就交给WEB框架来做。
# 用python开发一个web框架十分容易，所以python有上百个开源的web框架，这里我们先不讨论各种web框架的优缺点，直接选择一个比较流程的web框架--
# Flask来使用
# 用Flask编写web app比WSGI接口简单，我们先用easy_install或者pip安装Flask
# 然后写一个app.py来处理3个UR，分别是：
#   GET /：首页返回Home
#   GET /signin：登录也，显示登录菜单
#   POST /signin：处理登录表单，显示登录结果
# 注意，同一个URL /signin分别有GET和POST两种请求，映射到两个处理函数中
# Flask通过python的装饰器在内部自动地把URL和函数给关联起来，所以，我们写出来的代码就像这样
# -*- coding: UTF-8 -*-
import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>HOME</h1>'


@app.route('/signin', methods=['GET'])
def signin_from():
    return '''<form action="/signin" method="POST">
               <p><input name="username"></p>
               <p><input name="password" type="password"></p>               
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

    # # 实际的web app应该拿到用户名和口令后，去数据库查询再对比，来判断用户是否能登录成功
    # # 除了Flask，常见的python web框架还有
    #     Django：全能型web框架
    #     web.py：一个小巧的web框架
    #     Bottle：和Flask类似的web框架
    #     Tomado：Facebook的开源异步web框架
    # 小结
    # 有了web框架，我们在编写web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数，这样，编写Web App就更加简单了
    # 在编写URL函数处理时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的，Web框架都提供了自己的API来实现这些功能，
    # Flask通过request.from['name']来获取表单内容
