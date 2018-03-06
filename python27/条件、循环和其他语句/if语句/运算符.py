#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#相等运算符
print 1==1

#is   同一性运算符  is运算符判定的是同一性而不是相等性，变量x和y被绑定到同一列表上，而z被绑定在另外一个具有相同值的列表
#它们的值是相等的 ，但是他们不是同一个对象
x=y=[1,2,3]
z=[1,2,3]
print x is y
print x is z
print y is not z

#in  成员组个运算符
a='jslafdjfkls'
b='fd'
c='13'
print b in a
print c in a

#字符串比较序列比较
print '-----------字符串比较-------------'
print 'aBc' == 'abc'
print 'aBc'.lower() == 'abc'.lower()
print '-----------序列比较-------------'
a=[1,2]
b=[2,1]
print a==b
print a<b
print a.sort()==b.sort()

#布尔运算符
#and运算符就是所谓的布尔运算符，他连接两个布尔值，并且在两个都为真时返回真，否则返回假
#or和not
print '-----------布尔运算符-------------'
number=input('Enter a number between 1 and 10 :')
if number <= 10 and number >= 1 :
    print 'Great'
else:
    print 'Wrong'

if number > 10 or number < -1 :
    print 'Hello'
else:
    print 'World'

a = ''
if not a:
    print 111111
else:
    print 2222222

# 断言,assert语句，  如果需要去报程序中的某个条件一定为真才能让程序正常工作，那么assert语句就有用了
#assert 可以在程序中置入检查点，天剑后可添加字符串，用来解释断言：
age = -1
assert 0<age<100,'测试断言，age必须是1-99之间的整数'


