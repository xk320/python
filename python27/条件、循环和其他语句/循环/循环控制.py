#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# #跳出循环
# #有些时候可能提前中断一个循环进行一个新的迭代，或者仅仅就是想结束循环
# #break
# #结束循环可以使用break语句
from math import sqrt
# for n in (range(99,0,-1)):
#     root=sqrt(n)
#     print n,root
#     if root == int(root):
#         print n
#         break
#
# #continue 让当前的迭代结束，跳到下一轮循环
# for n in range(10):
#     if n == 3:
#         continue
#     print n
#
# #while true/break语句联系
# while True:
#     word=raw_input('please input your name: ')
#     if not word:
#         break
#     print 'Hello,my friend %s!' % word

#循环中的else子句,else仅在没有调用break时执行
for n in range(99,81,-1):
    root=sqrt(n)
    if  root == int(root):
        print n
        break
else:
    print "Didn't find it"

#pass  什么都没有发生，通常当占位符来使用

#del 删除函数
x=['Hello','World']
y = x
y[1] = 'Python'
print x
print y
del x
print y
#x和y指向同一个列表，但是删除x并不会影响y，原因是删除的只是名称而不是列表本身的值。
#在python中没有办法直接删除值，也不需要过多考虑删除值的问题，python解释器会负责回收内存