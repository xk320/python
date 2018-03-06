# -*- coding: UTF-8 -*-
# 在多线程环境下，每个线程都有自己都数据，一个线程使用自己都局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全
# 局变量的修改必须加锁。但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦。
#
# def process_student(name):
#     std=Student(name)
#     #std是局部变量，但是每个汉东湖都要用它，因此必须传递下去
#     do_task_1(std)
#     do_task_2(std)
#
# def do_task_1(std):
#     do_subtask_1(std)
#     do_subtask_2(std)
#
# def do_task_2(std):
#     do_subtask_1(std)
#     do_subtask_2(std)
# 每个函数一层一层调用都这么传参数那还了得？用全局变量也不行，每个线程处理不同都Student对象，不能共享
import threading

local_school = threading.local()


def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.currentThread().name)


def process_thread(name):
    # 绑定threadlocal的student
    local_school.student = name
    process_student()

t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2=threading.Thread(target=process_thread,args=('Lily',))
t1.start()
t2.start()
t1.join()
t2.join()

#全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，但
# 是每个属性如local_school.student都是线程都局部变量，可以任意读写而互不干扰，也不用管理锁的问题
#可以理解为全局变量local_school是以个dict，不但可以用local_school.student，还可以绑定其他变量，如果local_school.teacher等等
