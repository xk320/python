#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# SQLite是一种嵌入式数据库，他的数据库就是一个文件，经常被集成到各种应用程序中，python就内置了SQLite3，不需要安装即可使用
# 表示数据库中存放关系数据的集合，一个数据库里通常都包含多个表，要操作关系型数据库，首先需要链接到数据库，一个数据库链接
# 成为connection,连接到数据库后需要打开游标，称之为cursor，通过cursor执行SQL语句，然后获取执行结果
# python定义了一套数据库操作的API接口，任何数据库要链接到python只需要提供符合Python标准的数据库驱动即可。
# 由于SQLite的驱动内置在python标准库中，所以我们可以直接来操作SQLite数据库。
# 实例：
import sqlite3
import traceback

# 连接到SQLite数据库，
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('test.db')
# 创建一个cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
try:
    cursor.execute('CREATE TABLE user (id varchar2(20) PRIMARY KEY ,name varchar2(40))')
except sqlite3.OperationalError:
    pass
# 继续执行一条语句
try:
    cursor.execute('INSERT INTO user (id,name) VALUES ("1","Michael")')
except sqlite3.IntegrityError as e:
    pass

try:
    cursor.execute('INSERT INTO user (id,name) VALUES ("2","JACK")')
except sqlite3.IntegrityError as e:
    pass

# 查询表记录
cursor.execute('SELECT * FROM user')
# 获取查询到的结果集
values = cursor.fetchall()
print values
# 如果SQL语句都带有参数，那么需要吧参数按照位置传递给execute()方法，有几个？占位符，就必须对应几个参数，例如：
cursor.execute('SELECT * FROM user WHERE id=? AND name =?', ('1', 'Michael'))
values = cursor.fetchall()
print values, '-' * 8
# 通过rowcount获取插入的行数
print cursor.rowcount
# 关闭cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭数据库链接
conn.close()

# 使用python的db-ap时，只要搞清楚connection和cursor对象，打开后一定记得关闭，就可以放心的使用了。
# 使用cursor对象执行insert、update、delete语句的时候，执行结果由rowcount返回影响的行数，就可以拿到执行结果
# 使用cursor对象执行select语句是，通过featchall()可以拿到结果集，结果集是一个list，每个元素都是一个tuple，对应一条记录
