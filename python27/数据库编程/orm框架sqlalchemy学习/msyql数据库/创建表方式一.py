#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# 创建实例，并连接test库
engine = create_engine("mysql+pymysql://root:123456@localhost/test",
                                    encoding='utf-8', echo=True)
# echo=True 显示信息
Base = declarative_base()  # 生成orm基类

class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine) #创建表结构 （这里是父类调子类）

# 运行，显示相关信息，包括生成的sql语句：
#
# CREATE TABLE user (
#     id INTEGER NOT NULL AUTO_INCREMENT,
#     name VARCHAR(32),
#     password VARCHAR(64),
#     PRIMARY KEY (id)
# )