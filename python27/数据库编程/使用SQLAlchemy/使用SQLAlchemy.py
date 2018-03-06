#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#数据库是一个二维表，包含多行多列，把一个表的内容用python的数据结构表示出来的话，可以用一个list表示多行，list的每个元素是
#tuple，表示一行记录，比如包含id和name的user表
    # [
    #     ('1', 'Michael'),
    #     ('2', 'Bob'),
    #     ('3', 'Adam')
    # ]
#python的DB-AP返回的数据结果就是像上面这样表示的
#但是用tuple表示一行很难看出表的数据结构，如果吧一个tuple用class实例来表示，就可以更容易的看出表的结构来：
    # class User(object):
    #     def __init__(self):
    #         self.id=id
    #         self.name=name
    # [
    #     User('1', 'Michael'),
    #     User('2', 'Bob'),
    #     User('3', 'Adam')
    # ]
#这就是传说中的ROM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上
#但是有谁来做这个转换，所以ORM框架应运而生。
#在python中最有名的ORM框架是SQLAlchemy
#第一步，导入SQLAlchemy，并初始化DBSession
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#创建对象的基类
Base=declarative_base()

#定义User对象
class User(Base):
    #表名字
    __tablename__='user'
    #表结构
    id = Column(String(20),primary_key=True)
    name=Column(String(40))

#初始化数据库链接
engine=create_engine('mysql+mysqlconnector://root:root@39.106.182.219:3306/test')
DBSession=sessionmaker(bind=engine)
#以上代码完成SQLAlchemy的初始化和具体每个表的class定义，如果有多个表，就继续定义其他class
#create_engine()用来初始化数据库连接，SQLAlchemy用一个字符串表示连接信息：
#'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'