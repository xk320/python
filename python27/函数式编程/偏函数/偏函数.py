# -*- coding: UTF-8 -*-
import functools

# python的functools莫款提供来很多有用的功能，其中一个就是偏函数（partial function），要注意这里的偏函数和
# 数学意义上的偏函数不一样，在介绍函数参数的时候，通过设定参数的默认值，可以降低函数调用的难度，而偏函数也可以
# 做到这一点，距离如下：int（）函数可以把字符串转换成正式，当仅传入字符串时，int（）函数默认按十进制转换
print int('123456')
# 但int（）函数还提供额外的base参数，默认值为10，如果传入base参数，就可以做进制的转换：
print int('12345', base=8)
print int('12345', 16)


# 假设要转换大量的二进制字符串，每次都传入int(x,base=2)非常麻烦，我们可以定义一个int2()的函数，默认把base=2
# 传进去

def int2(x, base=2):
    return int(x, base)


# 这样转换二进制就非常方便了。
print int2('1000000')
# functools.partial就帮助我们创建一个偏函数，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函
# 数int2:
int22 = functools.partial(int, base=2)
print int22('100000')
# 简单总结 functools.partial的作用就是把一个函数的某些参数给固定住，返回一个新的函数，调用这个新的函数会更简单
# 注意上面的新的int22函数，不仅仅把base参数重新设定默认值为2，但也可以在函数掉入是传入其他值
print int22('11111', base=10)

# 创建偏函数时实际上可以接收函数对象、*args和**kw这3个单数，当传入：int22=functools.partial(int,base=2)实际
# 上固定来int()函数的关键字base，也就是int('10010')相当于kw={base:2} int('10010',**kw)
# 当传入 max2=functools.partial(max,10)实际上把10作为*args的一部分自动加到左边，
# 也就是max2(5,6,7)相当于args=(10,5,6,7) max(*args)结果为10

# 总结，当函数的参数个数太多，需要简化时，，使用functools.partial可以创建一个新的函数，这个新的函数可以固定原函数
# 的部分参数，从而在调用是更简答
