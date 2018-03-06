# -*- coding: UTF-8 -*-
# 正常情况下，当我们定义类一个class，创建了class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性，先定义一个class：
class Student(object):
    def __init__(self):
        pass


# 给实例添加一个属性
s = Student()
s.name = 'Micheal'
print s.name


# 还可以尝试给实例绑定一个方法：
def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s, Student)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print s.age

#但是给一个实例绑定一个方法，对另外一个实例不起作用
s2=Student()
try:
    s2.set_age(22)
except Exception as e :
    print e

#为了给所有实例绑定方法，可以给class绑定方法：

def set_score(self,score):
    self.score=score

Student.set_score=MethodType(set_score,None,Student)
s.set_score(80)
print s.score
s2.set_score(90)
print s2.score

#通常情况下set_score方法可以直接写在class类中，但是动态绑定允许我们在程序运行的过程中动态给class添加上功能