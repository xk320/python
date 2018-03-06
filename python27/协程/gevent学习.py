# -*- coding: UTF-8 -*-
# python通过yield提供了对协程的节本支持，但是不完全，而第三方的gevent为python提供了比较完善的协程支持
# gevent是第三方，通过greeniet实现协程，基本思想是：
# 党一个greeniet遇到IO操作时，比如访问网络，就自动切换到其他的greeniet，等到IO操作完成，再在适当的时候切换回来继续执行，由于IO操作非常耗
# 时，经常程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greeniet在运行，而不是等待IO
# 由于切换是在IO操作时自动完成，所以gevent需要修改python自带的一些标准库，这一过程在启动时通过monkey path完成
#     from gevent import monkey;monkey.patch_socket()
#     import gevent
#     def f(n):
#         for i in range(n):
#             print gevent.getcurrent(), i
#     g1 = gevent.spawn(f,5)
#     g2 = gevent.spawn(f,5)
#     g3 = gevent.spawn(f,5)
#     g1.join()
#     g2.join()
#     g3.join()
# 通过执行结果可以看出，三个greenlet是一次运行而不是交替运行
# 要让greenlet交替运行，可以通过gevent.sleep()交出控制权
#     import gevent
#     def f(n):
#         for i in range(n):
#             print gevent.getcurrent(),i
#             gevent.sleep(0)
#     g1 = gevent.spawn(f,5)
#     g2 = gevent.spawn(f,5)
#     g3 = gevent.spawn(f,5)
#     g1.join()
#     g2.join()
#     g3.join()
# 三个greenlet交替运行
# 把循环次数改为500000，让它们的运行时间长一点，然后在操作系统的进程管理器中看，线程数只有1个
# 当然实际代码里，我们不会用gevent.sleep()去切换协程，而是在执行到IO操作时，gevent自动切换，代码如下：
from gevent import monkey;

monkey.patch_all()
import gevent
import urllib2


def f(url):
    print 'GET: %s' % url
    resp = urllib2.urlopen(url)
    data = resp.read()
    print '%d bytes received from %s .' % (len(data), url)


gevent.joinall([
    gevent.spawn(f, 'http://www.163.com/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
# 从结果看，3个网络操作是并发执行的，而且结束顺序不同，但只有一个线程
# 小结
# 使用gevent，可以获得极高的并发性能，但gevent只能在unix或linux下运行，在windows下不保证正常安装和运行
# 由于gevent是基于IO切换的协程，所以最神奇的是，我们编写web app代码，不需要引入gevent的包，也不需要修改任何代码，仅仅在部署的时候，用一个
# 支持gevnet的WSGI服务器，立刻就获得了数倍的性能提升，具体部署方式可以参考后续实战 部署Web APP
