#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket
import sys

HOST = 'localhost'
PORT = 8002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'socket created'
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bing Failed.Error code is %s  Message :%s' % (str(msg[0]), msg[1])
    sys.exit()

print 'Socket bing complete'

s.listen(20)
print 'Socket now listening'

conn, addr = s.accept()
print 'Connected with %s:%s' % (addr[0],str(addr[1]))

date = conn.recv(1024)
conn.sendall(date)
conn.close()
s.close()
