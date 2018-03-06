# -*- coding: UTF-8 -*-
#__iter__ 一个特殊的方法，这个方法时迭代器规则（iterator protocol）的基础
#__iter__方法返回一个迭代器（interator）所谓的迭代器就是具有next方法（这个方法在调用时不需要任何参数）的对象。在调用next方法时，迭代器会
# 返回她的下一个值。如果next方法被调用，但迭代器没有值可以返回，就会引发一个StopIteration异常。
#备注：迭代器规则在python3。0中有一些变化，在新的规则中，迭代器对象应该实现 __next__方法，而不是next。而新的内建函数next可以用于访问这个
# 方法。换句话说next(it) 等同于3.0之前版本中的it.next()
#迭代器的关键时不使用列表，因为列表的杀伤力太大，如果有一个函数，可以一个接一个的计算值，那么在使用时可能计算一个值时获取一个值，而不是通过
# 列表一次性获取所有值。如果有很多值，列表就会占用太多的内存。   使用迭代器更通用、更简单、更优雅。
#斐波那契数列，使用迭代器如下：
class Fibs:

    def __init__(self):
        self.a, self.b = {0, 1}

    def next(self):
        self.a,self.b = self.b,self.a + self.b
        return self.a

    def __iter__(self):
        return self
#一个实现了__iter__方法的对象时可以迭代的，一个实现类next方法的对象则是迭代器
#下文中先创建一个对象，在for循环中使用该对象，查找在斐波那契数列中比1000大的最小数是多少
fibs = Fibs()
for i in fibs:
    if  i > 1000:
        print i
        break

# 从迭代器得到序列
#处理在迭代器和可迭代对象上进行迭代，还能把他们转化为序列。在大部分能使用序列的情况下都能使用迭代器替换：
class TestIterator:
    value = 0
    def next(self):
        self.value += 1
        if  self.value > 10 :
            raise StopIteration
        return self.value
    def __iter__(self):
        return self
testlist = TestIterator()

print list(testlist)
