# -*- coding: UTF-8 -*-
import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in ['AAA','BBB','CCCC']:
    c.sendto(data,('127.0.0.1',8888))
    print c.recv(1024)
c.close()