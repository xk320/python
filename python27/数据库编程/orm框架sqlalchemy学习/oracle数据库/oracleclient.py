#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, MetaData
from sqlalchemy.orm import sessionmaker, mapper

# 创建数据库链接实例
#定义引擎
engine = create_engine('oracle://python:python@127.0.0.1/orcl')
#绑定元信息
metadata = MetaData(engine)
Base=declarative_base()
#创建表格，初始化数据库
user = Table('usercode', metadata,
             Column('id', Integer, primary_key=Table),
             Column('name', String(75)),
             Column('password', String(90))
             )

class User(object):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

metadata.create_all(engine)
# 如果表已经存在就不在创建表
mapper(User, user)

# 创建数据库回话
session_class = sessionmaker(bind=engine)
Session = session_class(bind=engine)

#添加记录
# user_obj=User(id=27,name='IVY',password='123456')
# Session.add(user_obj)
# try:
#     Session.commit()
# except Exception as e :
#     print e.message.decode('gbk')

#查询记录
class DCOMINFO(Base):
    __tablename__='D_COM_INFO'
    comid=Column('COM_ID',String(80),primary_key=True)
    compid=Column('COM_PID',String(80))
    comname=Column('COM_NAME',String(1000))
    insuresysid=Column('insure_sys_id',String(10))
    comlevel=Column('com_level',String(80))
    upperpath=Column('upper_path',String(1000))
    def __repr__(self):
        return self.comid,self.comlevel

# res=Session.query(DCOMINFO).all()
res = Session.query().filter()
for line in res:
    try:
        print line.comid,'-'*10,line.comname.decode('gbk').encode('utf8')
    except :
        print line.comid, '-' * 10, line.comname
