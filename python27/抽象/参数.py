#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#在def语句中函数名后面的变量通常叫做函数的形参，而调用函数的时候提供的值叫做实参
#当参数是字符串的时候，在函数内为参数赋值不会改变外部任何变量的值
def try_to_change(n):
    n='Mr Gumbyu'
name='Mrs Entity'
try_to_change(name)
print name
#参数存储在局部作用域（local scope）内

#当参数是可变的数据结构（如列表），函数内部重新复制将改变列表中对应的键值
def list_change(n):
    n[0]='Mr Gumbyu'
name=['Mrs Entity','Mrs Haha']
print name
list_change(name)
print name

#当参数是以列表等可变的数据结构进行传递时，为保证数据的安全可以通过切片的方式建立副本进行传递
print '-'* 45
def list_change_qie(n):
    n[0]='Mr Gumbyu'
    print n
name1=['Mrs Entity','Mrs Haha']
print name1
list_change_qie(name[:])
print name1

#位置参数、关键字参数、参数收集、关键字参数收集
def test(name,*args,**kwargs):
    print '位置参数--------',name
    # print '关键字参数------',num
    print '参数收集成元组----',args
    print '参数收集到字典----',kwargs
test('Jack',1,2,3,4,x=1,y=2,z=3)
print '-'*8,'传说中的分割线','-'*8
def test1(*args,**kwargs):
    print args
    print kwargs
    print dict(args[0])
alist=[1,2,3,4,5,6,7]
adict={'Lucy':12,'Jack':18,'Lily':20}
# test1(alist)
test1(adict)

