# -*- coding: UTF-8 -*-
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例，因此，错误并不是凭空产生的，而是有意创建并抛出的。python的内
# 置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好集成关系，然后用raise语句抛出一个错误的实例：
class FooError(StandardError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value : %s' % str(s))
    return 10 / n


# foo(0)
# 执行可以最后跟踪到我们自己定义的错误：_main__.FooError: invalid value : 0
# 只有在必要的时候才定义我们自己的错误类型，如果可以选择python已有的内置的错误类型，尽量使用python内置的错误类型

# 另一种错误处理的方式
def too(s):
    n = int(s)
    return 10 / n


def far(s):
    try:
        return too(s) * 2
    except StandardError as e:
        print 'Error!'
        raise


def main():
    far('0')


main()
# 在bar()函数中，我们明明已经捕获了错误，但是打印一个error后，有吧错误通过raise语句抛出去了，
# 这种错误处理方式非常常见，捕获错误目的只是记录一下，便于后续追踪，但是由于当前函数不知道应该怎么处理改错误，所以恰当的
# 方式是继续往上抛，让顶层调用者处理。
# raise语句如果不带参数，就会把当前错误原样抛出，此外在except中raise一个Error，还可以把一种类型的错误转换成另外一种类型
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。
