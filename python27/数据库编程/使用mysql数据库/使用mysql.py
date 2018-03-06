#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# mysql是web世界中使用最广泛的数据库服务器，SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。mysql
# 是为服务器端设计的数据库，能承受高并发访问，同时zhany8ong的内存也远远大于SQLite。
# 此外，mysql内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB
# 连接数据库
# 导入mysql驱动
import mysql.connector, traceback

conn = mysql.connector.connect(user='root', password='123456', database='test', use_unicode=True)
cursor = conn.cursor()
# 创建user表
try:
    cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
except Exception:
    pass
try:
    cursor.execute('insert into user (id, name) values (%s,%s)', ['1', 'JACK'])
except Exception:
    pass
cursor.execute('select * from user where id = %s', ['1'])

res = cursor.fetchall()
print res
print cursor.rowcount
conn.commit()
cursor.close()
