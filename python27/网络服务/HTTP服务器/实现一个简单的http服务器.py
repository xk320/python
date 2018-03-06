#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket,signal,errno
from time import sleep

def HttpResponse(header,whtml):
    f = file(whtml)
    contxtlist=f.readlines()
    context=''.join(contxtlist)
    response='%s %d\n\n%s\n\n' % (header,len(context),context)
    return response

def sigInHander(signo,frame):
    print 'get signo#',signo
    global  runflag
    runflag = False
    global lisfd
    lisfd.shutdown(socket.SHUT_RD)

strHost='localhost'
HOST = strHost
PORT=8080
httpheader='''
27.HTTP/1.1 200 OK 
28.Context-Type: text/html 
29.Server: Python-slp version 1.0 
30.Context-Length: '''
lisfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lisfd.bind((HOST,PORT))
lisfd.listen(2)

signal.signal(signal.SIGINT,sigInHander)

runflag = True
while runflag:
    try:
        confd,addr = lisfd.accept()
    except socket.error as e:
        if e.errno == errno.EINTR:
            print 'get a except EINTR'
        else:
            raise
        continue

    if runflag == False:
        break;

    print "connect by ",addr
    data = confd.recv(1024)
    if not data:
        break
    print data
    confd.send(HttpResponse(httpheader,'index.html'))
    confd.close()
else:
    print 'runflag#',runflag

print 'Done'

