# -*- coding: UTF-8 -*-
# 高阶函数除了可以接收函数作为参数外，还可以把函数作为结果值返回。我们来实现一个可变参数的求和。通常情况下
# 求和的函数是这样定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 但是如果不需要立刻求和，而是在后面的代码中，根据需要在计算怎么办？可以不返回求和的结果，而是返回求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1, 3, 5, 7, 9)
print f
# 调用函数f时，才真正计算求和的结果
print f()

# 在这个例子中，我们在函数lazy_sum中又定义来函数sum，并且内部函数sum可以引用外部函数lazy_sum的参数和局部
# 变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为 闭包 （Closure）的程序结构
# 拥有极大的威力。
# 再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1 == f2


# 闭包
# 注意到返回的函数在其定义内部引用局部变量args，所以当一个函数返回一个函数后，其内部局部变量还被新函数引用，
# 所以闭包用起来简单，实现起来不容易
# 另一个需要注意的问题是，返回的函数并没有立即执行，而是直到调用时才执行，看一个例子：
def countt():
    fs = []
    for b in range(1, 4):
        def a():
            return b * b

        fs.append(a)
    return fs


a1, a2, a3 = countt()
print a1(), a2(), a3()
# 在上面的例子中，每次循环都创建一个新的函数，然后把创建的3个函数都返回来。
# 你可能认为调用f1(),f2(),f3()结果应该是1，4，9，但实际结果是 9，9，9，因为等到3个函数都返回时，他们
#所引用都变量i已经变成了3，因此最终结果为9
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量，
# 如果一定要引用循环变量怎么办？方法就是在创建一个函数，用该函数的参数绑定循环变量当前的值，无论循环变量
#后续如何更改，已经绑定到的函数参数的值不变：

def counttt():
    fs=[]
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs
b1,b2,b3=counttt()
print b1(),b2(),b3()

