# -*- coding: UTF-8 -*-
# 面向对象最重要的概念就是类calss和实例instance，必须牢记类是抽象的模版，比如student类，而实例是根据类创建出来的一个个具体的对象，每个对
# 象都拥有相同的方法，但各自数据可能不同
# class后面紧跟着是类的名字 student，紧接着是（object），表示该类是从哪里继承的。
class student(object):
    # 由于类可以起到模版的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去，通过定义一个特殊的__init__方法，在创建实
    # 例的时候进行属性绑定，
    # 注意__init__方法的第一个参数永远都是self，表示创建的实例本身

    # 数据封装
    # 面向对象编程的一个重要特点就是数据封装，在上面的student类中，每个实例就拥有各自的name和score这些数据，我们可以通过函数来访问这些数据，比
    # 如打印学习成绩。但是既然student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在student类的内部定义访问
    # 数据的函数，这样就把数据给封装起来了，这些封装数据的函数是和student类本身是关联起来的，我们称之为类的方法：
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_sc(self):
        print '%s : %s' % (self.name, self.score)

    def get_grade(self):
        if self.score > 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


a = student('lll', 91)
b = student('ccc', 59)
c = student('ddd', 67)
print a.get_grade()
print b.get_grade()
print c.get_grade()

# 总结
# 类是创建实例的模版，而实例则是一个一个具体的对象，哥哥实例用欧的数据都互相独立，互不影响
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据
# 通过在实例上调用方法，我们就直接操作类对象内部的数据，但无需直到方法内部的实现细节
# 和静态语言不同，python允许对实例变量绑定任何数据，也就是说对与两个实例变量，虽然他们都是同一个类的不同实例，但拥有但变量名称都不可能相同
# a.age=9
# print a.age
# print b.age
