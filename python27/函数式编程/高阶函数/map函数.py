# -*- coding: UTF-8 -*-
# map函数接收两个参数，一个是函数，一个是序列，map将传入的函数一次作用到序列的每个元素，并把结果作为新的
# list返回。
# 举例说明，比如我们有一个函数f(x)=x*x，要把这个函数作用在一个list[1,2,3,4,5,6,7]上，就可以用map实现
def f(x):
    return x * x
print map(f,[1,2,3,4,5,6,7,8,9])
#map()传入的第一个参数是f，即函数对象本身，map（）作为高阶函数，事实上它把运算规则抽象了，我们不单可以计
# 算简单的f(x)=x*x，还可以计算任意复杂的函数，比如把这个list所有数字转换为字符串
print map(str,[1,2,3,4,5])

#练习，利用map（）函数，把用户输入的不规范的英文名字变为首字母大写其他小写的规范名字
L=['adam', 'LISA', 'barT']
def Capi(a):
    return a.capitalize()
print map(Capi,L)