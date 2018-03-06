# -*- coding: UTF-8 -*-
# Socket是网络编程的一个抽象概念，通常我们用一个socket表示打开了一个网络链接，而打开一个socket需要知道目标计算机的IP地址和端口号，在指定协
# 议类型即可
# 客户端
# 大多数连接都是可靠的TCP连接，创建TCP连接时，主动发起连接的叫做客户端，被动响应连接的叫服务器
# 当我们在浏览器中访问新浪时，计算机就是客户端，浏览器会主动向新浪的服务器发起连接，服务器接收了我们的连接一个TCP连接就建立起来了。

# 导入socket库
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn', 80))
# 创建socket时，AF_INET指定使用IPV4协议，如果要用更先进的IPV6，就指定AF_INET6,SOCK_STREAM指定使用面向流的TCP协议。这样一个socket就创
# 建成功，但是还没有建立起连接。
# 客户端主动发起TCP连接，必须知道服务器的IP地址和端口号，注意连接服务器代码参数是一个tuple，包含地址和端口号。
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#TCP连接创建的是双向通道，双方都可以同时给对方发数据，但是谁先发谁后发怎么协调，要根据具体的协议来决定，HTTP协议规定客户端必须先发请求给服
# 务器，服务器收到后才发数据给客户端。发送的文本格式必须符合HTTP标准，如果格式没有问题，接下来就可以接口服务器返回的数据来
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=''.join(buffer)
#接收数据时调用recv(max)方法，一次最多接收指定的字节数，因此在一个while循环中反复接收直到接收完毕退出循环。
#当我们接收完数据后，调用close()方法关闭socket，这样一次完整的网络通信就结束来
s.close()
#接收到的数据包包括http头和网页本身，我们只需要把HTTP头和网页本身分离，打印出HTTP头，将网页保存到文件。
header,html=data.split('\r\n\r\n',1)
print header
with open('sina.html','wb') as f:
    f.write(html)