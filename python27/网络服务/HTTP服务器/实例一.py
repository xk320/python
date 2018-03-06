#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket
HOST,PORT='192.168.1.103',8081
listen_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listen_socket.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listen_socket.bind((HOST,PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection,client_address=listen_socket.accept()
    requset=client_connection.recv(1024)
    print requset
    #响应状态行TTP/1.1 200 OK包含了HTTP版本，HTTP状态码和HTTP状态码理由短语OK。浏览器得到响应时，它就显示响应的body，
    # 所以你就看到了“Hello, World！”
    http_response='''
HTTP/1.1 200 OK

Hello World!
    '''
    client_connection.sendall(http_response)
    client_connection.close()