# -*- coding: UTF-8 -*-
#httplib是一个相对底层的http请求模块，urllib就是基于httplib封装的，简单使用如下：
import httplib
conn = httplib.HTTPConnection('www.python.com')
conn.request('GET','/index.html')
r1 = conn.getresponse()
print r1.status,r1.reason
data1=r1.read()
conn.request('GET','/parrot.spam')
r2 = conn.getresponse()
data2 = r2.read()
conn.close()