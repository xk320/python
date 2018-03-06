# -*- coding: UTF-8 -*-
#首先编写hello.py，实现web应用程序的WSGI处理函数：
def application(environ,start_response):
    start_response('200 OK',[('Content-type','text/html')])
    return '<h1>Hello World!</h1>'

def application_1(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print environ['PATH_INFO'][1:]
    print environ
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

