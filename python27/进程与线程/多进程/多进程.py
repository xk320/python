# -*- coding: UTF-8 -*-
# 要让python程序实现多进程（multiprocessing),先了解操作系统相关知识
# Unix/Linux操作系统提供一个fock()系统调用，它非常特殊。普通的函数调用调用一次返回一次，但是fock()调用一次，返回两次，因为操作系统自动把
# 当前进程（称为父进程）复制一份（称为子进程），然后分别在父进程和子进程内返回。
# 子进程永远返回0，父进程返回子进程的I。这样做的理由是一个父进程可以fock出很多子进程，所以父进程要记下每一个子进程的I，而子进程需要调用getpid()
# 就可以拿到父进程的I。
# python的os模块封装类常见的系统调用，其中就包括fock，可以在python程序中轻松创建子进程
import os

print 'Process (%s) start ....' % os.getpid()
pid = os.fork()
if pid == 0:
    print 'I an child process (%s) and my parent is %s .' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just created a child process (%s) .' % (os.getpid(), pid)
# 运行结果如下：
# Process (4427) start ....
# I (4427) just created a child process (4428) .
# I an child process (4428) and my parent is 4427 .
# 由于windows没有fork调用，上面的代码在Windows上无法运行，由于mac系统是基础BSD内核，所以mac下运行是没有问题的。
# 有类fock调用，一个进程在接到新任务时就可以复制出一个子进程处理新任务，常见的apache服务器就是有父进程监听端口，每当有新的http请求时，就
# fork出子进程来处理新的http请求。
