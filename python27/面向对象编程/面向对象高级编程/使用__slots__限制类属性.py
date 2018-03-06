# -*- coding: UTF-8 -*-

# 使用__slots__
# 但是，如果我们想要限制class的属性怎么办？比如只允许Student实例添加age和name属性。
# 为了达到限制的目的，python允许在定义class的时候定义一个特殊的__slots__变量，来现实该class能添加的属性：
class Student(object):
    __slots__ = ('name', 'age')

    def __init__(self):
        pass


s = Student()
s.name = 'Micheal'
s.age = 25
print s.name, s.age

try:
    s.score = 100
except Exception as e:
    print e


# 由于score没有添加到__slots__中，所以不能绑定score属性
# 使用__slots__要注意，__slots__属性只对当前类起作用，对继承对子类不起作用

class GranduateStudent(Student):
    pass


g = GranduateStudent()
g.score = 100
print g.score
