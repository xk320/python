# -*- coding: UTF-8 -*-

# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型的，有那些方法？
# 使用type()，判断对象类型
a = 123
b = '123'
print type(a), type(b)


# 如果变量指向的是函数或者类，也可以用type()判断：
class Aaaa(object):
    def run(self):
        print 'aaa'


A = Aaaa()
B = Aaaa.run
print type(A)
print type(B)

# 但是type()函数返回的是什么类型呢？它返回的是type类型，如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：

print type(123) == type(234)

# 但是这种写法太麻烦，python把每种type类型都定义好类敞亮，放在types模块中，使用之前需要先导入：
import types

print '_' * 80
print type(123) == types.IntType
print type('123') == types.StringType
print type([])==types.ListType
print type(str)==types.TypeType
#注意最后一种TypeType类型，所有类型本身就是TypeType，比如：
print type(int)==type(str)==types.TypeType