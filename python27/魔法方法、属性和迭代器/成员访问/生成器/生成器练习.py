# -*- coding: UTF-8 -*-
#这里有必要说一下multitask模块（不是标准库中的），看看multitask使用的简单代码：
import Queue
def tt():
    for x in xrange(4):
        print 'tt'+str(x)
        yield
def gg():
    for x in xrange(4):
        print 'gg'+str(x)
        yield

# t=multitask.TaskManager()
# t.add(tt())
# t.add(gg())
# t.run()

#输出结果：tt0
# xx0
# tt1
# xx1
# tt2
# xx2
# tt3
# xx3
#如果不是使用生成器，那么要实现上面的现象，即函数交替输出只能使用线程了，所以生成器给我们提供了更广阔的前景
#如果仅仅实现上面的效果其实很简单，我们可以自己写一个，主要思路就是将生成器对象放入队列，执行send(None)后如果没有抛出StopIteration
#将该生成器对象在加入队列
class Task:
    def __init__(self):
        self._queue = Queue.Queue()

    def add(self,gen):
        self._queue.put(gen)

    def run(self):
        while not self._queue.empty():
            for i in xrange(self._queue.qsize()):
                try:
                    gen = self._queue.get()
                    gen.send(None)
                except StopIteration:
                    pass
                else:
                    self._queue.put(gen)

t = Task()
t.add(tt())
t.add(gg())
t.run()