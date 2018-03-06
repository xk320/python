#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#异常和函数能很自然的一起工作，如果异常在函数内引发而不被处理，他就会传播至函数调用的地方，如果在哪里也没有处理异常，它就会继续传播。
# 一直到达主程序，如果哪里没有异常处理程序，程序就会带着栈跟踪之中
def faulty():
    raise Exception('Something is wrong!')
def ignore_exception():
    faulty()
def handle_exception():
    try:
        faulty()
    except:
        print 'Exception handled'

# ignore_exception()
handle_exception()

