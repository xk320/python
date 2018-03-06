# -*- coding: UTF-8 -*-
# 多线程和多进程最大的不同在于，多进程中，同一个变量各自有一份拷贝存在与每个进程中，互不影响，而多线程中，所有变量都是有所有线程共享，所以任
# 何一个变量都可以被任何一个线程修改。因此线程之间共享数据最大的微信在于多个线程同时修改一个变量，把内容给改乱了。
# 举例说明多个线程同时操作一个变量怎么把内容给该乱了
import multiprocessing, threading

# 假设这是银行存款
balance = 0
balance1 = 0


def change_it(n):
    global balance
    # 先存后取，结果应该为0
    balance = balance + n
    balance = balance - n


def change_it1(n):
    global balance1
    # 先存后取，结果应该为0
    balance1 = balance1 + n
    balance1 = balance1 - n


def run_thread(n):
    for i in range(10000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
# 定义了一个共享变量balance，初始值是0，并且启动两个线程先存后取，理论上结果应该是0，但是由于线程的调用是有操作系统决定的，当t1、t2交替执行
# 时，只要循环次数足够多，balance的结果就不一定是0了，因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
# balance=balance+n 也分两步
# 1、计算balance，存入临时变量中
# 2、将临时变量的值赋给balance。
# 究其原因是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多线程把同一个对象的内容改乱了。
# 如果我们要确保balance计算正确，就要给change_it() 上一把锁，当某个线程开始执行change_it() 时，我们说改线程因为获得了锁，因此其他线程不
# 能同时执行change_it() ，只能等待直到锁被释放后，获得该锁以后才能改，由于锁只有一个，无论多少线程，同以时刻最多只有一个线程持有该锁，所以
# 不会造成修改的冲突，创建一个锁就是通过threading.Lock()来实现：
lll = threading.Lock()


def run_thread1(n):
    for i in range(100000):
        lll.acquire()
        try:
            change_it1(n)
        finally:
            lll.release()


t3 = threading.Thread(target=run_thread1, args=(5,))
t4 = threading.Thread(target=run_thread1, args=(8,))
t3.start()
t4.start()
t3.join()
t4.join()
print balance1
# 当多线程同时执行lock.acquire()时，只有一个线程能成功的获取锁，然后继续执行代码，其他线程就继续等待直到直到获得锁为止
# 获得锁的线程用完后一定要释放锁，否则其其它线程将永远等待下去，成为死线程。所以我们用try：... finally来确保一定会释放锁
# 锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码只能以单线程模
# 式执行，效率就大大地下降来，其次由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多线程全部挂起，
# 既不能执行也无法结束。只能依靠操作系统强行终止。

# 多核CPU
# 如果你不幸拥有一个多核CPU，你肯定在想，多核应该可以同时执行多个线程。
# 如果写一个死循环的话，会出现什么情况呢？
# 打开Mac OS X的Activity Monitor，或者Windows的Task Manager，都可以监控某个进程的CPU使用率。
# 我们可以监控到一个死循环线程会100%占用一个CPU。
# 如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。
# 要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。
def loop1():
    x=0
    while True:
        x=x+1
for i in range(multiprocessing.cpu_count()):
    t=threading.Thread(target=loop1)
    t.start()
#启动与CPU核心数相同的N个线程，在4核CPU上可以监控到CPU占用率仅60%，也就是使用不到两核心
#启动100个线程，使用率也就170%左右仍然不到两核心
#但是C\C++或java来改写相同的死循环，直接可以个全部核心跑满，为什么python不行？
#因为python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何python线程执行前，必须先获取GIL锁，
#然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在
# Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
# GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。
# 所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
# 不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

# 小结
# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。

