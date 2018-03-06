# -*- coding: UTF-8 -*-
#我们可以看到，gun()不是函数调用，而是产生生成器对象
def gun():
    for x in xrange(4):
        tmp = yield x
        if  tmp == 'Hello':
            print 'World!'
        else:
            print str(tmp)

g = gun()
print g

#生成器对象支持集中方法，next(),send(),throw()
#调用生成器next()方法，将运行到yield位置，此时暂停执行环境并返回yield后到值。所以打印出来到是0，暂停执行环境。
print g.next()
#再次调用next()方法，为啥会打印出两个值：上次调用next()执行到yield 0暂停，再次执行恢复环境，给tmp赋值（注意：这里的tmp的值不是x的值，而
# 是通过send方法接受的值），由于我们没有调用send方法，所以tmp值为None，此时输出的是None，并执行下一次yield x，所以又输出1
print g.next()

#send方法
print g.send('Hello')
#上次执行到yield 1后停止，此时我们send('Hello'),并给tmp赋值为'Hello',此时tmp=='Hello'为真，所以输出'World!'并执行到yield 2，所以又
# 打印出2（ next()等价于 send(None) ）