# -*- coding: UTF-8 -*-
# 在class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样就隐藏了内部的的复杂逻辑
# 但是，从前面student类的定义来看，外部代码还是可以自由修改一个实例的name和score属性
# 如果要让内部属性不被外部访问，可以把属性的名称前面加上两个下划线__，在python中实例的变量名如果以__开头，就变成一个私有变量（private），
# 只有内部可以访问，
class student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s : %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 < score <= 100:
            self.__score=score
        else:
            raise ValueError('bad score!')

# 修改完成后对于外部代码来说没有改动，但是已经无法从外部访问实例变量__name和__score了：
a = student('aaa', 98)
a.print_score()
try:
    print a.__name
except AttributeError as e:
    print e

# 这就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

# 但是如果外部代码要获取name和score怎么办？可以给student增加get_name 和 get_score这样的方法：
print a.get_name()
print a.get_score()

#但是如果外部代码要修改score怎么办？可以增加set_score方法
a.set_score(100)
a.print_score()
try:
    a.set_score(1000)
except Exception as e :
    print e