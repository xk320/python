# -*- coding: UTF-8 -*-

# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人用，有的函数和变量我们希望仅仅在模块内使用，在python中，通过_
# 前缀来实现。正常的函数和变量名是公开的（public），可以被直接引用
# 类似__xxx__这样的变量是特殊变量，可以被直接引用但是有特殊用途
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
# 之所以我们说，private函数和变量不应该被直接引用，而不是不能被直接引用，是因为python并没有一种方法可以完全限制访问private函数或变量，但
# 从编程习惯上不应该引用private函数或变量，private函数或变量不应该被别人引用，那他们有什么作用？

def _private_1(name):
    return 'Hello %s !' % name

def _private_2(name):
    return 'Hi %s !' % name

def greeting(name):
    if len(name)>3:
        print _private_1(name)
    else:
        print _private_2(name)

#我们在模块力公开greeting（）函数，而把内部逻辑用private函数隐藏起来，这样调用greeting函数不用关心内部private函数细节，这也是一种非常常
# 用的代码封装和抽象方法，即：外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public
