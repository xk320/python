#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
stime = time.time()
f = open('e:\\tjmx.txt','r')
n = open('e:\\tjfx.txt','w')
lines = f.readlines()
dd = {}
for line in lines:
    a = line.strip('\n').split(' ')
    dd.setdefault(a[0],[])
    dd[a[0]].append(a[1])
f.close()
for i in range(0,len(dd)) :
    c = dd.popitem()
    # print(c[0],'\n')
    n.write(c[0])
    n.write(' ')
    n.write( ",".join(c[1]))
    n.write( '\n')
n.close()
etime=time.time()
print('总用时%.2f秒' % (float(etime-stime)))



