# -*- coding: UTF-8 -*-
# 如果不捕获错误，自然可以让python解释器来打印出错误堆栈，但程序也被结束来。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，
# 同时让程序继续执行下去
# python内置的logging模块可以非常容易的记录错误信息：
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)


main()
print 'END'
