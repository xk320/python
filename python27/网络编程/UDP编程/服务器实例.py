# -*- coding: UTF-8 -*-
import socket, threading, logging
from myutils.systemLogger import Outlog

logger=Outlog()
server_addr = '127.0.0.1'
server_port = 8888
tcpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcpserver.bind((server_addr, server_port))
print
while True:
    data, addr = tcpserver.recvfrom(1024)
    rdate = 'Hello, %s . Welcome!' % data
    logger.loginfo(rdate)
    tcpserver.sendto(rdate, addr)

