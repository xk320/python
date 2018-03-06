#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey,create_engine
from sqlalchemy.orm import mapper
engine = create_engine("oracle://python:python@127.0.0.1/orcl")
metadata = MetaData()

user = Table('user', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50)),
            Column('fullname', String(50)),
            Column('password', String(12))
        )

class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

mapper(User, user)  # 类User 和 user关联起来
# the table metadata is created separately with the Table construct,
# then associated with the User class via the mapper() function
# 如果数据库里有，就不会创建了。