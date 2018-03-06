#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
c=factorial(999)

print c


