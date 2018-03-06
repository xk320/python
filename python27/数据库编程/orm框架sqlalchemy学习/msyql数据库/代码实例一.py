#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker

# 创建实例，并连接test库
engine = create_engine("mysql+pymysql://root:123456@localhost/test",
                       encoding='utf-8')
Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "[%s name:%s]" % (self.id, self.name)


class Student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    stu_id = Column(Integer)
    age = Column(Integer)  # 整型
    gender = Column(Enum('M', 'F'), nullable=False)

    def __repr__(self):
        return "[%s stu_id:%s sex:%s]" % (self.stu_id, self.age, self.gender)


Session_class = sessionmaker(bind=engine)
Session = Session_class()  # 生成session实例

res = Session.query(User, Student).filter(User.id == Student.stu_id).all()
print(res)
