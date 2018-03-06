# -*- coding: UTF-8 -*-
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信，python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes
# 等多种方式来交换数据。
# 以Queue为例，在父进程中创建两个子进程，一个往Queue李写数据，一个从Queue里读取数据：
import multiprocessing
import os, time, random


# 写数据进程执行代码
def write(q):
    for i in ['a', 'b', 'c']:
        print 'Put %s to queue ....' % i
        q.put(i)
        time.sleep(random.random())


# 读数据进程执行代码
def readf(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue .' % value


if __name__ == '__main__':
    # 父进程创建Queue，并传给子进程
    q = multiprocessing.Queue()
    pw = multiprocessing.Process(target=write, args=(q,))
    pr = multiprocessing.Process(target=readf, args=(q,))
    # 启动子进程pw，写入
    pw.start()
    # 启动子进程pr，读取
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程是死循环，无法等待其结束，只能强行终止
    pr.terminate()


# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，multiprocessing
# 需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，
# 要先考虑是不是pickle失败了。
