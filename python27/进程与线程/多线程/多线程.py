# -*- coding: UTF-8 -*-
# 多任务可以有多进程完成，也可以由多线程完成。
# 我们前面提到来进程是由若干个线程组成的，一个进程至少又一个线程
# 由于线程是操作系统支持的执行单元，因此高级语言通常都内置多线程的支持，python是真正的Posix Thread，而不是模拟出来的线程。
# python标准库提供来两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行来封装，绝大多数情况下我们只需要使
# 用threading这个高级模块
# 启动一个线程及时把一个函数传入并创建thread实例，然后调用start()开始执行：
import time,threading
#新线程执行代码
def loop():
    print 'thread %s is running .....' % threading.current_thread().name
    n=0
    while n < 5:
        n=n+1
        print 'thread %s >>>> %s' % (threading.current_thread().name,n)
        time.sleep(1)
    print 'thread %s ended . ' % threading.currentThread().name

print 'thread %s is running ...' % threading.currentThread().name
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.currentThread().name
# 执行结果如下：
# thread MainThread is running ...
# thread LoopThread is running .....
# thread LoopThread >>>> 1
# thread LoopThread >>>> 2
# thread LoopThread >>>> 3
# thread LoopThread >>>> 4
# thread LoopThread >>>> 5
# thread LoopThread ended .
# thread MainThread ended.

#由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，python的threading模块有个current_thread()函数，它永
# 远返回当前线程的实例。主线程的实例名称叫MainThread，子线程的名字在创建的时候指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，
#完全没有其他意义，如果不其名字，python就会自动给线程命名为Thread-1、Thread-2。。。。。
