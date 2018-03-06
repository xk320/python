#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#为了引发异常，可以使用一个类（应该是exception的子类）或者实例参数调用raise语句。
#下面的例子引发了一个没有任何有关错误信息的普通异常
#raise Exception
#下面的例子引发异常后添加了错误信息
#raise Exception('This is a Exception`test!')
#内建的异常类有很多。Python库参数手册的Built-in Exceptions 一节中有关于他们的描述。
#用交互式解释器也可以分析他们，这些内建异常都可以在exceptions模块（和内建的命名空间）中找到。
#可以使用dir函数列出模块的内容
import exceptions
print dir(exceptions)

#重要的内建异常类
#Exception   所有异常的基类
# #AttributeError 特性引用或赋值失败时引用
# IOError   试图打开不存在的文件（包括其他情况）时引发
# IndexError    在使用序列中不存在的索引时引发
# KeyError    在使用映射中不存在的键时引发
# NameError   在找不到名字（变量）是引发
# SyntaxError     在代码为错误形式时引发
# TypeError   在内建操作或者函数应用于错误类型的对象时引发
# ValueError  在内建操作或者函数应用于正确类型的对象，但是该对象使用不合适的值时引发
# ZeroDivisionError   在除法或者模除操作的第二个参数为0时引发