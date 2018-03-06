# -*- coding: UTF-8 -*-
# 现在有一个简单的还书myfunc，想通过代码得到这个函数的大概执行时间
import time


def deco(func):
    def wrapper():
        starttime = time.time()
        func()
        endtime = time.time()
        msecs = (endtime - starttime) * 1000
        print '-> elapsed time : %f ms' % msecs
    return wrapper

@deco
def myfunc():
    print 'start myfunc'
    time.sleep(0.6)
    print 'end myfunc'



myfunc()
