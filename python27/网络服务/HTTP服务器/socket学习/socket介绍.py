#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# seocket起源于linux，而Unix/Linux基本哲学之一是  一切皆文件  ，对于文件用打开、读写、关闭模式来操作。socket就是该模式的
# 一个实现，socket即是一种特殊的文件，一些socket函数就是对其进行的操作（读写IO、打开、关闭）
# 基本上，Socket是任何一种计算机网络通讯中最基础的内容，例如当你在浏览器地址栏输入：http://192.168.1.103时，你会打开一个
# 套接字，然后连接到http://192.168.1.103并读取响应的页面并显示出来，而其他一些聊天客户端如skype也是类似的，任何网络通讯都
# 是通过Socket来完成的
# Socket与file的区别：
# 1、file模块是针对某个指定文件进行打开、读写、关闭
# 2、socket模块时针对服务器和客户端secket进行打开、读写、关闭
# 创建流套接字描述符  —> bind 命名套接字（协议、地址、端口）—> listen监听客户端socket请求

# socket服务端简单实例一
import socket
import sys

# 函数 socket.socket 创建一个 socket，返回该 socket 的描述符，将在后面相关函数中使用。
# 该函数带有两个参数：
#  Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）
# Type：套接字类型，可以是 SOCKET_STREAM（流式套接字，主要用于 TCP 协议）或者SOCKET_DGRAM（数据报套接字，主要用于 UDP 协议）
# 如果创建 socket 函数失败，会抛出一个 socket.error 的异常，需要捕获：
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket.Error code: %s   Error message: %s' % (msg[0], msg[1])
    sys.exit()
print 'Socket Created'
