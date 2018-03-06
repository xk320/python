# -*- coding: UTF-8 -*-
# 在Thread和Process中，应当优选Process，因为更稳定，而且Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的错CPU上
# python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上去，一个服务进程可以作为调度，将任务分布其
# 他多个进程中，依靠网络通信。由于managers模块封装好，不必了解网络通讯的细节，就可以很容易的编写分布式多进程程序。
# 举个例子：如果我们已经一个通过queue通信的多进程程序在同一台机上运行，现在由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程
# 分布到两台机器上，怎么用分布式进程实现？原有的queue可以继续使用，但是，通过managers模块把queue通过网络暴露出去，就可以让其他机器的进程
# 访问queue 了
# 我们先看服务进程，服务进程负责启动queue，把queue 注册到网络上，然后往quequ里面写入任务：
import  random,time,Queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue=Queue.Queue()
#接收结果的队列
result_queue=Queue.Queue()

#从basemanager继承的QueueManager：
class QueueManager(BaseManager):
    pass

#把两个queue都注册到网络上，callable参数关联queue 对象
QueueManager.register('get_task_queue',callable=lambda :task_queue)
QueueManager.register('get_result_queue',callable=lambda :result_queue)
#绑定端口5000，设置验证码abc
manager= QueueManager(address=('',5000),authkey='abc')
#启动queue
manager.start()
#获得通过网络访问的queue对象
task=manager.get_task_queue()
result=manager.get_result_queue()
#放几个任务进去
for i in range(10):
    n =random.randint(0,10000)
    print 'Put task %d...' % n
    task.put(n)
#从result队列读取结果：
print 'Try get results .....'
for i in range(10):
    r=result.get(timeout=10)
    print 'Result : %s ' % r

#这个简单的manager/worder模型有什么用？其实这就是一个简单但真正但分布式计算，把代码稍加改造，启动多个worker，就可以把任务分布几台甚至几
# 十台机器上，比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。
#Queue对象存储在哪？worker中根本没有创建Queue的代码，所以Queue对象存储在manager进程中
#而Queue之所以能通过网络访问，就是通过QueueManager实现，由于QueueManager管理的不知一个Queue，要给每个Queue的网络调用接口起个名字
#authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果taskworker.py的authkey和taskmanager.py的authkey不一致，肯
# 定连接不上。

#小结
#python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多态机器的环境下。
#注意Queue作用是用来传递任务和接收结果，每个任务描述数据要尽量小，比如发送一个处理日志文件的任务，就不要发送几百M的日志文件本身，而是发送日
# 志文件存放的路径，有worker进程再去共享的磁盘读取文件