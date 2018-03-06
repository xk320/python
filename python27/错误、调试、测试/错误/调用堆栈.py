# -*- coding: UTF-8 -*- 
# 如果错误没有被捕获，它就会一直往上抛，最后被python解释器捕获，打印出一个错误信息，然后程序退出
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def mail():
    bar(0)


mail()
# 出错不可拍，可怕的是不知道哪里出错来，解读错误信息就是定位错误的关键，我们从上往下可以看到整个错误的调用函数链
# 错误信息第一行Traceback (most recent call last):  高速我们这个错误的跟踪信息
# Traceback (most recent call last):
#   File "/Users/mac/Desktop/study_python/python27/错误、调试、测试/调用堆栈.py", line 15, in <module>
#     mail()
#   File "/Users/mac/Desktop/study_python/python27/错误、调试、测试/调用堆栈.py", line 12, in mail
#     bar(0)
#   File "/Users/mac/Desktop/study_python/python27/错误、调试、测试/调用堆栈.py", line 8, in bar
#     return foo(s)*2
#   File "/Users/mac/Desktop/study_python/python27/错误、调试、测试/调用堆栈.py", line 4, in foo
#     return  10 / int(s)
# ZeroDivisionError: integer division or modulo by zero
# 调用mail()出错了，代码文件是xxx第15行，但原因是第12行
# 调用bar(0)出错来，在代码文件但第12行，但原因是第8行
# return foo(s) * 2 出错来，但这不是最终原因，继续往下看
# return 10 / int(s)这个语句出错了，这是错误产生的源头，根据错误类型ZeroDivisionError，我们判断，int(s)本身并没有出错，但是int(s)返
# 回0，在计算10 / 0时出错，至此，找到错误源头。
