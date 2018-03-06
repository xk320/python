# -*- coding: UTF-8 -*-

# 当子类和父类都存在相同的方式时，子类覆盖父类方法，这样我们就获得了继承的另一个好处，多态：
class Print111(object):
    def run(self):
        print 111


class aaa(Print111):
    def run(self):
        print 'aaa'


a = aaa()

# 判断a的类型既可以是Print111，也可以是aaa，这是a就是多态的
print isinstance(a, Print111)
print isinstance(a, aaa)


# 要理解多态的好处，需要写一个函数，这个函数可以接收Print111类型的变量：

def run_twice(Print111):
    Print111.run()
    Print111.run()


run_twice(Print111())
run_twice(aaa())


# 看上去没上面意思，如果我们在定义一个bbb类型，也是从Print111派生：
class bbb(Print111):
    def run(self):
        print 'bbb'


run_twice(bbb())

# 新增的Print111的子类，不必对run_twice()做任何修改，实际上任何以来Print111作为参数的函数或者方法都可以不加修改的正常运行，原因就是多态
# 多态的好处就是，当我们需要传入aaa、bbb。。。时，只需要接收Print111类型就可以了，因为aaa、bbb都是Print111类型，按照Print111类型进行
# 操作即可，由于Print111类型有run()方法，因此，传入的任意类型，只要是Print111的类或者子类，就会自动调用实际类型的run()方法,这就是多态

# 对于一个变量，我们只需要直到它是Print111的类型，无需确切的直到它的子类型，就可以放心的调用run()方法，具体调用的run()方法是Print111、
# aaa、bbb对象上，有运行时该对象的确切类型决定，这就是多态的真正威力：调用方只管调用不管细节。而当我们新增一个Print111的子类时，只要确保
# run()方法编写正确，不用管原来的代码是如何调用的，这就是著名的"开闭"原则：
# 对扩展开放：允许新增Print111子类
# 对修改封闭：不需要修改依赖Print111类型的run_twice()等函数，继承还可以一级一级地继承下来，

#总结
#继承可以把父类的所有功能直接拿过来，子类只需要新增自己特有的方法，也可以把父类不合适的方法覆盖重写：
#有类继承，才能有多态。在调用类实例方法的时候，尽量把变量视作父类类型，这样所有子类类型都可以正常被接收
#旧的方式定义Python类允许不从object类继承，但是这种变成方式已经严重不推荐使用，如果没有合适的类可以继承，就继承自object类