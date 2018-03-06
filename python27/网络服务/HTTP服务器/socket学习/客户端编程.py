#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 获取服务器IP地址
import socket
import sys

host = 'localhost'
port = 8001
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print 'Hostname could not be resolved.Exiting'
    sys.exit()

print 'Ip address of %s is %s' % (host, remote_ip)

# 现在我们知道了服务器的 IP 地址，就可以使用连接函数 connect 连接到该 IP 的某个特定的端口上了，下面例子连接到 80 端口
# 上（是 HTTP 服务的默认端口）：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remote_ip, port))
print 'Socket Connected to %s on ip %s !' % (host, remote_ip)

# 发送数据
message = 'GET /HTTP/1.1\n\r\n'

try:
    s.sendall(message)
except socket.error:
    print 'Send failed.'
    sys.exit()
print 'Message send successfully'

# 接收数据
reply = s.recv(1024)
print reply
# 当我们不想再次请求服务器数据时，可以将该 socket 关闭，结束这次通信：
s.close()
