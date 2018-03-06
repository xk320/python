#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def recursion(*args):
    alist=['a', 'b', 'c', 'd', 'e']
    blist=['0', 'a', 'b', 'c', 'd']
    cdict=dict(zip(alist, blist))
    if cdict[args[0]]=='0':
        return cdict[args[0]]
    else:
        return recursion(cdict[args[0]])
c=recursion('d')
print c




a=list([(a,b,c) for a in range(1,7) for b in range(1,7) for c in range(1,7)])
b=[]
for index,value in enumerate(a):
    if a[index][0]!=a[index][1]  and  a[index][1]!=a[index][2]  and  a[index][0]!=a[index][2]:
        c=list(a[index])
        c.sort()
        if c not in b:
            b.append(c)
print len(b)
print b

#阶乘函数
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

#幂运算函数
def power(x,n):
    result=1
    for i in range(n):
        result*=x
    return result
print power(8,2)

#二分法查找
