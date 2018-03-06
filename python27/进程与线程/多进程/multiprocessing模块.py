# -*- coding: UTF-8 -*-
# Process
# 如果打算编写多进程的服务程序，Unix/Linux无疑是正确的选择，由于windows没有fork调用，难道在windows上就无法用python编写多进程程序来？
# 由于python是跨平台的，multiprocessing模块就是跨平台版本的多进程模块
# multiprocessing模块提供一个process类来代表一个进程对象，下面是演示了启动一个子进程并等待其结束：
import multiprocessing
import os


# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s) ...' % (name, os.getpid())

    # if __name__ == '__main__':
    #     print 'Parent process %s.' % os.getpid()
    #     p = multiprocessing.Process(target=run_proc, args=('test',))
    #     print 'Process will start.'
    #     p.start()
    #     p.join()
    #     print 'Process end .'

    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建比fock()还要简单。
    # join()方法可以等待子进程结束后在继续往下运行，同城用于进程间的同步


# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
import time, random


def long_time_task(name):
    print 'Run task %s (%s) ...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Tack %s runs %0.2f seconds .' % (name, (end - start))


if __name__ == '__main__':
    print 'Parent process %s .' % os.getpid()
    p = multiprocessing.Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done ...'
    p.close()
    p.join()
    print 'All subprocesses done.'
#对Pool对象调用join()方法会等所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
#注意输出结果，task0，1，是立刻执行的，而task2，3，4要等待前面某个task完成后才执行，这是因为Pool的默认大小当前电脑上默认是2，因此最多同
# 时执行2个进程，这是Pool有意设计的限制，并不是操作系统的限制，如果改成：p=Pool(5),就可以同时跑5个进程。
#由于Pool的默认大小是CPU的核心数，如果你不行拥有8核心CPU至少要条9个子进程才能看到等待效果。

