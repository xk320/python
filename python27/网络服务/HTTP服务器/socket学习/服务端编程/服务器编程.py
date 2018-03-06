#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 服务器端主要做以下工作：
# 打开 socket
# 绑定到特定的地址以及端口上
# 监听连接
# 建立连接
# 接收/发送数据

# 一、绑定socket
# 绑定完成之后，接下来就是监听连接了。
import socket
import sys

HOST, PORT = 'localhost', 8001
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket created'
except socket.error, msg:
    print 'Error code is %s :  Error message is %s' % (str(msg[0]), msg[1])
    sys.exit()

# try:
#     s.bind((HOST, PORT))
# except socket.error,msg:
#     print 'Error code is %s :  Error message is %s' % (str(msg[0]), msg[1])
#     sys.exit()
# print 'Socket bing complete'
s.bind((HOST, PORT))

# 二、监听链接
# 函数 listen 可以将 socket 置于监听模式：
# 该函数带有一个参数称为 backlog，用来控制连接的个数。如果设为 10，那么有 10 个连接正在等待处理，此时第 11 个请求过来时
# 将会被拒绝。
s.listen(10)
print 'Socket now listening'

#三、接收链接
#当有客户端向服务器发送连接请求时，服务器会接收连接：
conn,addr=s.accept()
print 'Connected with %s : %s' % (addr[0],addr[1])

