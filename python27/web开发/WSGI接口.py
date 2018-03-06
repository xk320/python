# -*- coding: UTF-8 -*-
# 了解HTTP协议和HTML文档，其实就是明白来一个web应用本质是：
# 1、浏览器发送一个HTTP请求
# 2、服务器收到请求，生成一个HTML文档
# 3、服务器把HTML文档作为HTTP响应的Body发送给浏览器
# 4、浏览器收到HTTP响应，从HTTP Body去除HTML文档并显示
# 所以，最简单的web应用就是先把HTML用文件保存好，用一个线程HTTP服务器软件，接受用户请求，从文件中读取HTML后返回。
# 如果要动态生成HTM，就需要把上述步骤自己来实现，不过接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没
# 开始动态HTML呢，就要个把月去读HTTP规范
# 正确的做法是底层代码有专门的服务器软件实现，我们用python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以要
# 一个统一的接口，让我们专心用python编写web业务。
# 这个接口就是WSG： Web Server Gateway interface
# WSGI接口定义非常简单，它只要求web开发者实现一个函数，就可以响应HTTP请求，我们来看一个最简单的web版本的Hello World！

# def application():
#     start_response('200 OK',[('Content-type','text/html')])
#     return '<h1>Hello World!</h1>'
# 上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
#   environ：一个包含所以HTTP信息的dict对象
# s tart_response：一个发送HTTP响应的函数
# 在application()函数中，调用start_response('200 OK',[('Content-type','text/html')])
# 就发送来HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数。start_response()接收两个参数，一个是HTTP
# 响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。
# 通常情况下，都应该把Content-Type头发送给浏览器，其他很多常用都HTTP Header也应该发送。
# 然后，函数返回值'<h1>Hello World!</h1>'将作为HTTP响应都Body发送给浏览器
# 有了WSG，我们关心的就是如何从envirom这个dict对象拿到HTTP请求信息，然后构造出HTM，通过start_response()发送Header，最后返回Body
# 整个application()函数本身没有涉及任何解析HTTP的部分，也就是说底层代码不需要我们编写，我们只负责在更高层次上考虑如何响应请求
# 不过这个application()函数怎么调用？如果我们自己调用，两个参数environ和start_response我们没法提供，返回的str也没法发给浏览器
# 所以application()函数必须有WSGI服务器来调用，很多符合WSGI规范的服务器，我们可以挑选一个用。但是现在，我们只想尽快测试一下我们编写的
# application()函数真的可以把HTML输到浏览器，所以要赶紧找一个最简单的WSGI服务器，把我们的web应用程序跑起来。
# python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯python编写的WSGI服务器的参考实现，所以参考实现是指该实现完全符合WSGI标准，但是
# 不考虑任何运行效率，进供开发和测试使用。

# 运行WSGI服务

# 首先编写hello.py，实现web应用程序的WSGI处理函数：
# def application():
#     start_response('200 OK',[('Content-type','text/html')])
#     return '<h1>Hello World!</h1>'

# 然后在编写一个server.py，负责启动WSGI服务器，加载application()函数
# 从wsgiref模块导入
from wsgiref.simple_server import make_server
# 导入我们编写的application函数
from hello import application_1

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application()
httpd = make_server('', 8000, application_1)
print 'Server HTTP on port 8000.....'
httpd.serve_forever()

# 在命令行可以看到wsgiref打印的log信息：
# 127.0.0.1 - - [19/Jan/2018 23:22:04] "GET / HTTP/1.1" 200 21
# 127.0.0.1 - - [19/Jan/2018 23:22:04] "GET /favicon.ico HTTP/1.1" 200 21

# 如果觉得这个web太简单了，可以稍微改造一下，从environ里读取PATH_INF，这样可以显示更加动态的内容
# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

# 小结
# 无论多负责的Web应用程序，入口都是一个WSGI处理函数，HTTP请求的所以输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()
# 加上函数返回值作为Body
# 负责都web应用程序，光靠一个WSGI函数来处理还是太底层，我们需要在WSGI之上再抽象出Web框架，进一步简化web开发
