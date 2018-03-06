#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 为了处理每个连接，我们需要将处理的程序与主程序的接收连接分开。一种方法可以使用线程来实现，主服务程序接收连接，创建
# 一个线程来处理该连接的通信，然后服务器回到接收其他连接的逻辑上来。
import socket
import sys
import thread
import logging
import threading

logger = logging.getLogger('socekt_server')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formater)
logger.addHandler(ch)

host = '127.0.0.1'
port = 8088

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as msg:
    print msg
    sys.exit()

s.listen(2)
logger.info('Socket now listening')


# 创建一个用于创建线程的函数
def clientthread(conn):
    # 连接成功发送消息
    conn.send('Welcome to the server. Type something and hit enter\n')
    # 创建循环让保持线程不结束
    while True:
        date = conn.recv(1024)
        reply = 'OK......' + date
        print date
        if date is None:
            break
        conn.sendall(reply)
    conn.close()


# 保持服务
while True:
    conn, addr = s.accept()
    logger.info('Connected with ' + addr[0] + ':' + str(addr[1]))
    thread.start_new_thread(clientthread, (conn,))
s.close()
