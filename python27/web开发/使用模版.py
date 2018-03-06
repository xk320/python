# -*- coding: UTF-8 -*-

# web框架把我们从WSGI中拯救出来，现在我们只需要不断的编写函数，带上UR，就可以继续web app的开发来
# 但是，web app不仅仅处理逻辑，展示给用户的界面也非常重要，在函数中返回一个HTML的字符串，简单的页面还可以，但是，想象新浪首页的6000多行HTM，
# 你确信能在python的字符串中正确地写出来吗？
# 俗话说得好，不懂前段的python工程师不是好的产品经理，有web开发经验的同学都明白，web app最复杂的部分就是在html页面，HTML不仅要正确，还要通
# 过CSS没话，在加上复杂的Javascript脚本来实现各种交互和动画效果，总之，生成HTML页面的难度很大。
# 由于在python代码李拼接字符串是不现实的，所以模版技术出现来
# 使用模版，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML ，而是嵌入了一些变量和命令，然后根据我们传入的数据替换后，得到最终
# HTM，发送给用户
# 浏览器发送请求    GET /Michael
#                                 name = 'Michael'
# app.py          @app.route('/<name>')
#                 def home(name):
#                     return render_template('home.html',name=name)
#
# 模版：       <html>
#                 <body>
#                     <p>Hello, {{ name }}!</p>
#                 </body>
#             </html>
#
#                 输出
#
# 用户看到：       <html>
#                     <body>
#                         <p>Hello, {{name}}!</p>
#                     </body>
#                 </html>
# 这就是传说中的MVC ，Model-View-Controller，中文名    模型-试图-控制器
# python处理URL的函数就是C ： Controller ，Controller负责业务逻辑，比如检验用户名是否存在，取出用户信息等等
# 包含变量 {{ name }}的模版就是V ： View，View负责显示逻辑，通过简答地替换一些变量，View最终输出的就是用户看到的HTML
# MVC中的Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出响应的数据
# 上个例子中，Model就是一个dict：   {'name':'Michael'}
# 现在，我们把上次直接输出自字符串作为HTML的例子用MVC模式改写一下：
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')
@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')
@app.route('/signin',methods=['POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='password':
        return render_template('sign-ok.html',username=username)

    return render_template('form.html',message='Bad username or password',username=username)

if __name__ == '__main__':
    app.run()

#Flask通过render_template()函数实现模版的渲染，和web框架类似，python的模版也有很多种，flask默认支持的模版是jinja2，所以我们也安装下
#然后开始编写jinja2模版
#
# home.html
# 用来显示首页的模板：
#
# <html>
# <head>
#   <title>Home</title>
# </head>
# <body>
#   <h1 style="font-style:italic">Home</h1>
# </body>
# </html>
# form.html
# 用来显示登录表单的模板：
#
# <html>
# <head>
#   <title>Please Sign In</title>
# </head>
# <body>
#   {% if message %}
#   <p style="color:red">{{ message }}</p>
#   {% endif %}
#   <form action="/signin" method="post">
#     <legend>Please sign in:</legend>
#     <p><input name="username" placeholder="Username" value="{{ username }}"></p>
#     <p><input name="password" placeholder="Password" type="password"></p>
#     <p><button type="submit">Sign In</button></p>
#   </form>
# </body>
# </html>
# signin-ok.html
# 登录成功的模板：
#
# <html>
# <head>
#   <title>Welcome, {{ username }}</title>
# </head>
# <body>
#   <p>Welcome, {{ username }}!</p>
# </body>
# </html>
# 登录失败的模板呢？我们在form.html中加了一点条件判断，把form.html重用为登录失败的模板。
# 通过MVC ，我们在python代码中处理M Model 和C  controller  而V ： View是通过模版处理的 ，这样我们就成功的把python代码和html代码最大
# 程度地分离了.使用模版的另一大好处是，模版该起来很方便，而且改完保存后，刷新浏览器就能看到最新的效果，这对于调试来说太重要了
# 比如循环输出页面
# {% for i in page_list %}
#    <a herf="/page/{{ i }}">{{ i }}</a>
# {% endfor %}
# 如果page_list是一个list：[1,2,3,4,5]，上面的模版将输出5个超链接
# 除了jinja2，常见的模版还有：
#   Mako： 用<% ... %>和${xxx}的一个模板；
#   Cheetah：也是用<% ... %>和${xxx}的一个模板；
#   Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
# 小结
# 有了MVC啊，我们就分离了python代码和HTML代码，HTML代码全部放到模版里，写起来更有效率