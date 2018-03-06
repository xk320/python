# -*- coding: UTF-8 -*-

# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是没办法检查参数，导致可以把成绩随便修改：
class Stu(object):
    pass


s = Stu()
s.score = 99


# 这样显然不和逻辑，为了限制score的范围，可以通过一个set_score()来设置成绩，在通过一个get_score()方法来获取成绩，这样就可以检查参数：
class Studentt(object):
    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('Score must be an integer!')
        if score > 100 or score < 0:
            raise ValueError('score must between 0 - 100 !')
        self.score = score

    def get_score(self):
        return self.score


# 现在，对任意对Student实例进行操作，都可以放心的设置score了
# 但是上面的方法又略复杂，没有直接用属性那么直接简单，通过装饰器 decorator 可以给函数动态加上功能，对于类的方法，装饰器一样起作用。
# python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('Score must be an integer!')
        if score > 100 or score < 0:
            raise ValueError('score must between 0 - 100 !')
        self._score = score


# @property的实现比较复杂，把一个getter方法变成属性，只要加上@property就可以类，此时@property本身又创建类另一个装饰器@score.setter，
# 负责把一个setter方法变成属性赋值，于是我们就拥有一个可控的属性操作：
s = Student()
s.score = 60
print s.score
try:
    s.score = 101
except Exception as e:
    print e


# 注意这到这个神奇的@property，我们在对实例属性操作对时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法实现的。
# 还可以定义制度熟悉过，只定义getter方法，不定义setter方法就是一个只读属性：
class Students(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        self._birth = birth

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        if not self.age:
            raise ValueError('age not exist ! ')
        del self._age


s = Students()
s.age = 55
print s.age
del s.age

# 上面的birth是可读写参数，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来

# 总结
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样程序运行就减少类出错的可能性。
