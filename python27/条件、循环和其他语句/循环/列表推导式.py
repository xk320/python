#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#列表推导式 是利用其它列表创建新的列表的一种方法
#新列表有range（10）中每个x的平方个组成
print [x*x for x in range(10)]
#新列表有range（10）中每个x的平方个组成，并且可以被3整除
print [x*x for x in range(10) if x % 3 == 0]
#增加更多的循环
print [(x,y) for x in range(10) for y in range(10)]
print len([(x,y) for x in range(112) for y in range(13)])
print len([(x,y,z) for x in range(112) for y in range(13) for z in range(20)])
#与if联合使用,循环两个列表，将名字首字母相同的人一同打印出来
girls=['alice','bernice','clarice']
boys=['chris','arnold','bob']
print [b+'+'+g for b in boys for g in girls if b[0] == g[0]]
