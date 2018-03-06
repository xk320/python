# -*- coding: UTF-8 -*-
# reduce把一个函数作用在一个序列[x1,x2,x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列
# 的下一个元素做累积计算，其效果就是reduce(f,[x1,x2,x3,x4]=f(f(f(x1,x2),x3),x4)
# 比如对一个序列求和就可以用reduce实现
def odd(x, y):
    return x + y


print reduce(odd, [1, 3, 5, 7, 9])


# 当然求和运算可以直接用python内建函数sum（），但是如果把序列换成整数13579，reduce就可以派上用场
def fn(x, y):
    return x * 10 + y


print reduce(fn, [1, 3, 5, 7, 9])


# 这个列子本身没有多大用处，但是如果考虑到字符串str也是一个序列，对上面对例子稍加改动，配合map()，我
# 们就可以写出把str转换为int的函数
def chartonum(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print reduce(fn, map(chartonum, '13579'))


# 整理成一个函数str2int
def str2int(s):
    def fnn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fnn,map(char2num,s))
print str2int('13579')

#还可以用lambda函数进一步简化

def Char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def Str2int(s):
    return reduce(lambda  x,y:x*10+y,map(Char2num,s))
print Str2int('23456')

#也就是说，假设python没有提供int（）函数，你完全可以自己写一个把字符串转换成整数的函数
#练习Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
def prod(L):
    def prod1(x,y):
        return x*y
    return reduce(prod1,L)
print prod([1,2,3,4,5,6])