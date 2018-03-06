# -*- coding: UTF-8 -*-

# 看到类似__slots__这种形式的__xxx__的变量或者函数名就要注意，这些在python种是有特殊用途的。
# __slots__我们已经知道怎么用来，__len__()方法我们也知道是为了让class作用与len()函数。
# 除此之外，python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
# __str__
# 我们先定义一个Student类，打印一个实例：
class Stud(object):
    def __init__(self, name):
        self.name = name


print Stud('Micheal')
# 打印出一堆<__main__.Student object at 0x109afb190>，不好看.怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串
# 就可以了：

class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

print Student('Micheal')

#但是上边的类直接敲变量不用print，打印出来的实例还是不好看，这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是
#__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调用服务的，解决办法是在定义一个
#__repr_()，但是通常__str__()和__repr__()代码都是一样但，所以偷懒写法如下：
class Students(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Students object (name: %s)' % self.name
    __repr__=__str__

print (Students('JAVA'))
Students('HAHA')