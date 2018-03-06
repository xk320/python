# -*- coding: UTF-8 -*-
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是变异时定义的而是运行时动态创建的。
# 比如我们要定义一个Hello的class，就写一个hello.py的模块
class Hello(object):
    def hello(self, name='world'):
        print 'Hello, %s.' % name


# 当python解释器载入Hello模块时，就会一次执行该模块的所以语句，执行结果就是动态创建出一个Hello的class对象，测试如下：
h = Hello()
h.hello()
print type(h)
print type(Hello)


# type()函数就可以查看一个类型或变量的类型,Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class hello
# 我们说class的定义是运行是动态创建的，而class的方法就是使用type()函数，type()函数即可以返回一个对象类型，又可以创建出
# 新的类型，比如我们可以通过type()创建出Hello类，而无需通过class Hello(object)...的定义
def fn(self, name='myworld'):
    print 'Hello , %s' % name


HELLO = type('HELLO', (object,), dict(hello=fn))  # 创建Hello class
a = HELLO()
a.hello()
# 要创建一个class对象，type()函数一次传入3个参数
# 1、class的名字
# 2、继承的父类集合，注意python支持多重继承，如果只有一个父类，别忘类tuple的元素写法
# 3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# 通过type()函数创建的类和直接写的class是完全一样的，因为python解释器遇到class定义时，仅仅是扫描一下class定义的语句，然
# 后调用type()创建出class
# 正常情况下，我们都用class XXXX 来定义类，但是type()函数也允许我们动态创建出类来，也就是说动态语言本身支持运行期动态创建类，
# 这和静态语言有非常大的不同，要在静态语言运行创建类，必须构造源代码在调用编译器，或者借助一些工具生成字节码实现
