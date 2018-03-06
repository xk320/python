#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 装饰模式有很多经典的使用场景，例如插入日志、性能测试、事务处理等等，有了装饰器就可以提取大量
# 函数中与本身功能无关的类似代码，从而达到代码重用的目的
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以通过变量也能调用函数
def now():
    print '2017-12-11'


f = now
f()
# 函数中有一个属性__name__，可以拿到函数的名字：
print now.__name__
print f.__name__


# 现在假设我们要增强now（）函数的功能，比如，在函数调用前后自动打印日志，但有不希望修改now()函数的定义，这种在代码运行期
# 间动态增加功能的方式，称之装饰器（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数，所以我们要定义一个能打日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kwargs):
        print 'call %s()' % func.__name__
        return func(*args, **kwargs)

    return wrapper


# 观察上面的log，因为它是一个decorator，所以接收一个函数作为参数并返回一个函数，我们借助python的@语法，把decorator置于函
# 数的定义处：
@log
def n():
    print '2017-01-11'


# 调用n()函数，不仅会运行n()函数，还会运行n()函数前打印一行日志
n()


# 由于log()是一个decorator返回一个函数，所以原来的n()函数仍然存在，只是现在执行n()将执行新函数，即log()函数返回的wrapper()
# wrapper()函数的参数定义是(*args, **kwargs)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，
# 再紧接着调用原始函数。
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def Log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@Log('execute')
def nn():
    print 'NNNNNN', nn.__name__


nn()
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：now=Log('execute')(nn)
# 首先执行Log('execute')，返回的是decorator函数，在调用返回的函数，参数是now函数，返回值最终是wrapper函数。
# 以上两种decorator的定义都没有问题，单还差最后一步，因为函数也是对象，它有__name__等属性，但去看经过decorator装饰之后的
# 函数，它们的__name__已经从原来的'now'变成了'wrapper'：因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函
# 数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的
# decorator的写法如下：
import functools


def lll(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print 'call %s():' % func.__name__
        return func(*args, **kwargs)

    return wrapper


def llll(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'call %s %s():' % (text, func.__name__)
            return func(*args, **kw)

        return wrapper

    return decorator


@lll
def nnn():
    print 'AAAAA', nnn.__name__


nnn()


@llll('name')
def nnnn():
    print 'name', nnnn.__name__


nnnn()

import time


def deco(arg):
    if arg:
        def _deco(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                stime = time.time()
                func(*args, **kwargs)
                etime = time.time()
                msecs = (etime - stime) * 1000
                print 'runtime : %f ms' % msecs

            return wrapper
    else:
        def _deco(func):
            return func
    return _deco


@deco(True)
def myfunc():
    print 'start %s' % myfunc.__name__
    time.sleep(1)
    print 'end'


@deco(True)
def addfunc(a, b):
    print 'start addfunc %s ' % addfunc.__name__
    time.sleep(1.2)
    print 'end addfunc'
    print 'result is %d' % (a + b)


myfunc()
addfunc(3, 8)


# 装饰器调用顺序
# 装饰器是可以叠加使用的，那么这就是设计到装饰器调用顺序了，对python中的@语法糖，装饰器的调用顺序与使用@
# 语法糖声明的顺序相反
def dero_1(func):
    print 'enter into dero_1'

    def wrapper(a, b):
        print 'enter into dero_1_wrapper'
        func(a, b)

    return wrapper


def dero_2(func):
    print 'enter into dero_2'

    def wrapper(a, b):
        print 'enter into dero_2_wrapper'
        func(a, b)

    return wrapper


@dero_1
@dero_2
def addfu(a, b):
    print 'result is %d ' % (a + b)


addfu(3, 3)
