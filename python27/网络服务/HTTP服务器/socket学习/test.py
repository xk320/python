# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket

obj = socket.socket()
obj.connect(("192.168.1.103",8080))

ret = str(obj.recv(1024),encoding="utf-8")
print(ret)