#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import cx_Oracle

tns = cx_Oracle.makedsn('127.0.0.1', '1521', 'orcl')
pythondb = cx_Oracle.connect('python', 'python')
cr = pythondb.cursor()
sql = 'select * from D_INSURE_SYS_INFO'
cr.execute(sql)
rs = cr.fetchall()
for line  in range(len(rs)):
    print 'print all:(%s %s)  ' % (rs[line][0],rs[line][1].decode('GBK').encode('utf8'))
cr.close()
pythondb.close()
