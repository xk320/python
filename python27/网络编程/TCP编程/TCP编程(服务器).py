# -*- coding: UTF-8 -*-
# 服务器进程首先要绑定一个端口并监听来自其他客户端的连接，如果某个客户端连接过来，服务器就与该客户端建立socket连接，然后通信就靠socket连接
# 所以服务器会打开固定的端口监听，每一个客户端连接就创建该socket连接，由于服务器会有大量来自客户端的连接，所以服务器要能够区分一个socket连
# 接是那个客户端绑定的。一个socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来确定一个socket
# 但是服务器还需要同时响应多个客户端的请求，所以每一个连接都需要一个新的进程或者新的线程来处理，否则服务器一次只能服务一个客户端。
# 编写一个简单的服务器程序，接收客户端连接，把客户端发来的字符串加上hello在发回去
# 一、创建一个基于IPV4和TCP协议的socket
import socket
import threading


# 每个链接都必须创建新线程或进程来处理，否则单线程在处理链接过程中，无法接受其他客户端的链接
def tcplink(sock, addr):
    print 'Accept new connection from %s:%s ....' % (sock, addr)
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        if data == 'exit' or not data:
            break
        sock.send('Hello ,%s' % data)
        print 'Hello ,%s' % data
    sock.close()
    print 'Connection from %s : %s Closed...' % (sock, addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 二、我们要绑定监听的地址和端口
s.bind(('127.0.0.1', 9998))

# 三、调用listen()方法开始监听端口，传入的参数指定等待链接的最大数量
s.listen(5)
print 'Waiting for connection.....'
# 接下来服务器通过一个永久循环来接受客户端的链接，accept()会等待并返回一个客户端链接
while True:
    # 接受新链接
    sock, addr = s.accept()
    # 创建新线程来处理tcp链接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()



# 建立链接后，服务器首先发送一条欢迎信息，然后等待客户端消息，并加上hello在发送给客户端，如果客户端发送exit字符串，直接关闭链接
