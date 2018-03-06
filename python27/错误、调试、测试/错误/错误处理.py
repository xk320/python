# -*- coding: UTF-8 -*-
# 在程序运行的过程中，如果发生来错误，可以实现约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错
# 误码非常常见。比如打开文件函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1
# 用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须大量的代码来判断是否出错：
# 一旦出错，还要一级一级上报，知道某个函数可以处理该错误（比如，给用户输入一个错误信息）。
# 所有高级语言通常都内置一套 try ... except ... finally ... 的错误处理机制，python也不例外
try:
    print 'try.....'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except :', e
finally:
    print 'finally.....'
print 'END'
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续直接跳转至错误代码处理，即except语句块，执行except后，如
# 果有fianlly语句块，则执行finally语句块，直至执行完毕。
# 从输出可以看出，当错误发生时，后续语句print 'result:', r不会被执行，except由于捕获到ZeroDivisionError，因此被执行，最后finally语句
# 被执行。
# 如果没有错误发生，except语句不会被执行，但是finally如果有，则一定会被执行。

#python的错误其实也是class，所有的错误类型都继承自baseexception，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其他子类的
# 也一网打尽，比如：
try:
    foo()
except StandardError as e:
    print 'StandardError'
except ValueError:
    print 'ValueError'
#第二个except永远不会被执行，因为ValueError是StandardError的子类，如果有，也被第一个except给捕获了
#Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：https://docs.python.org/2/library/exceptions.html#exception-hierarchy
#使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只
# 要main()捕获到了，就可以处理：
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        print 'Error!'
    finally:
        print 'finally...'
