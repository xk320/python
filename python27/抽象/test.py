#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import math
a=[0,1]
for n in range(8):
    a.append(a[-2]+a[-1])
print a

print fibs(8)
