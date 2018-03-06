# -*- coding: UTF-8 -*-

# 如果一个类想被用于 for ... in 循环，类似list或者tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后python的for循
# 环就会不断调用该迭代对象的next()方法拿到循环的下一个值，知道遇到StopIteration错误时退出
# 我们以斐波那契数列为例，写一个Fib类，可以作用于fo让循环：
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a、b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a


for i in Fib():
    print i


# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是把它当作list来使用还是不行，比如去第5个元素：
# 要表现的像List那样按照下标去出元素，需要实现__getitem__()方法：
class Fibb(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a


# 现在就可以按下标来访问数列的任意项来
print Fibb()[5], Fibb()[100]


# 但是list有个神奇的切片方法：对于Fibb报错，原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
class Fibbb(object):
    def __getitem__(self, item):
        a, b = 1, 1
        if isinstance(item, int):
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            L = []
            for x in range(stop):
                if x > start:
                    L.append(a)
                a, b = b, a + b
            return L


print Fibbb()[3:9]


# 但是没有对step参数作处理，也没有对负整数做处理，所以要确实实现一个__getitem__()还是有很多工作要做的，此外把对象看成dict，__getitem__
# 测参数也可能是一个可以做key的object，例如str，与之对应的 __setitem__方法，把对象视作list或者dict来对集合赋值。最后还有一个__delitem__
# 方法，用户删除某个元素。
# 通过上面对方法我们自己定义的类表现的于python自带的list、tuple、dict没上面区别，这完全归功于动态语言的鸭子类型，不需要抢到继承某个接口

