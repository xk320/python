# -*- coding: UTF-8 -*-
#TCP是建立可靠链接，并且通讯双方都可以以流都形式发送数据，相对TC，UDP则面向无连接都协议。
#使用UDP协议时，不需要建立连接，只需要直到对方的IP地址和端口号，就可以直接发送数据包，但是能不能到达不知道
#虽然用UDP传输数据不可靠，但它的有点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。
#服务器首先需要绑定端口
import socket

#创建socket时用SOCK_DGRAM指定UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定IP和端口和TCP一样，但是不需要listen()方法，而是直接接受来自客户端的数据
s.bind(('127.0.0.1',8888))
print 'Bind UDP port on 8888 .....'
while True:
    data,addr=s.recvfrom(1024)
    print 'Received from %s : %s' % (addr,data)
    s.sendto('Hello, %s !' % data,addr)
#recvfrom()方法返回数据和客户端地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。


