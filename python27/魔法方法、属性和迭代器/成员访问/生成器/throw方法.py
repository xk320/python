# -*- coding: UTF-8 -*-
def stop_immediately(name):
    if name == 'skycrab':
        yield 'OKOK'
    else:
        print 'NONO'

s = stop_immediately('sky')
# 由于NONO没有额外的yield，所以直接抛出异常StopIteration
#s.next()
#throw方法
def mygen():
    try:
        yield 'something'
    except ValueError:
        yield 'value error'
    finally:
        print 'clean'  #一定会被执行
gg=mygen()
print gg.next()
print gg.throw(ValueError)
#调用gg.next很明显输出'something'，并在yield 'something'暂停，此时gg发送ValueError异常，恢复执行环境except将会捕捉并输出信息。
#理解来这些我们就可以像协同程序发起攻击了，所以协同程序也是可以挂起、恢复，有多点进入，其实说白了也就是多个函数可以同时进行，可以相互之间发
# 送消息等