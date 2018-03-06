#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 现在在一个终端下运行下面的服务器程序，再开启三个终端，分别用 telnet 去连接，如果一个终端连接之后不输入数据其他终端是
# 没办法进行连接的，而且每个终端只能服务一次就断开连接。这从代码上也是可以看出来的。

import socket
import sys

host = 'localhost'
port = 8008

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((host, port))
except socket.error as msg:
    print msg

s.listen(2)
print 'Socket now listening'

while True:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    data = conn.recv(1024)
    reply = 'OK .... ' + data
    if not data:
        print '111111'
    conn.sendall(reply)

conn.close()
s.close()
