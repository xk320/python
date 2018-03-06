# -*- coding: UTF-8 -*-
# 通过列表表达式，我们可以直接创建一个列表。但是受到内存限制，列表容量肯定是有限的，而且，创建一个
# 包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，后面绝大多数元素
# 扎农空间都白白浪费来，所以如果列表元素可以按照某种算法推算出来，那么我们可以在循环都过程中不断推
# 算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大
# 量的空间。在python中，这种一边循环一边计算的机制，成为生成器（Generator）
# 要创建一个generator有很多中方法，第一种方法很简单，只要把一个列表表达式的[]改成（）即可
L = [x * x for x in range(10)]
print L
G = (x * x for x in range(10))
print G
# 创建L和G的区别仅在于最外层是[]和（），L是一个list G是一个generator
# 我们可以直接打印list中的元素，如何打印打印generator的每个元素？
# 如果一个一个打印出来可以通过genetator的next（）方法： G.next()
# next()不断调用太变态来，正确的方法是使用for循环：
for i in G:
    print i

#generator非常强大，如果推算的算法比较复杂，用类似列表推倒时的for循环无法实现的时候，可以用函数实现
#著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可以有前两个数想家得到
#斐波拉契数列用列表生成式写不出来，但是用函数把它打印出来去很容易：
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print b
        a,b=b,a+b
        n+=1
fib(6)

#仔细观察可以看出，fib函数实际上是定义来斐波拉契数列的推算规则，可以从第一个元素开始，推算除后续任意的
#元素，这种逻辑其实非常类似generator。也就是说，上面的函数和generator仅一步之遥，要把fib函数变成generator
#只需要把print b 改成yield b就可以来
def Fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n+=1
print Fib(6)
#这里最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或最后一行函数语句
#就返回。而变成generator的函数，每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回
#yield语句出继续执行，实例：
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5
o=odd()
print o.next()
print o.next()
print o.next()
#可以看出odd不是普通函数，而是generator。在执行过程中遇到yield就终中断，下次🈶️继续执行，执行3次yield
#后，已经没有yield可以执行来，所以第4次调用next（）就报错
#回到Fib的例子，我们在循环过程中不断调用yield，就会不断中断，当然要给循环设置一个条件来推出循环，不然
#就换产生一个无限数列出来。同样的把函数改成generator，我们基本上从来不会用next（）来调用它，使用for
for i in Fib(6):
    print i

#总结，generator是非常强大的工具，在python中可以简单的把列表生成式改成generator，也可以通过函数实现
#负责逻辑的generator