# -*- coding: UTF-8 -*-
import socket
import time
import traceback
HOST='39.106.182.219'
PORT=8088
ADDR=(HOST,PORT)
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(ADDR)
    print 'socket connection successed'
    i=1
    while True:
        msg='INFO %d \r\n' % i
        s.send(msg)
        i+=1
        time.sleep(0.5)
except Exception as e:
    print traceback.format_exc()

