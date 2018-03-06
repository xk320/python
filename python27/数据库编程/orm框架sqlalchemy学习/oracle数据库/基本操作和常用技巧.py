#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from sqlalchemy import create_engine, Column, func, or_, not_
from  sqlalchemy.orm import sessionmaker
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# db_connnect_string就是连接数据库的路径，python就是用户名密码，charset指定字符集可以省略，
db_connnect_string = 'oracle://python:python@127.0.0.1/orcl'
# create_engine创建一个数据库引擎，echo参数为True时，会显示每条执行SQL语句
engine = create_engine(db_connnect_string, echo=True)
# sessionmaker会生成一个数据库的类，这个类的实例可以当成一个数据库链接，它同时还记录了一些查询的数据，并决定什么时候执行
# SQL语句。由于SQLALchemy自己维护一个数据库连接池（默认5个链接），因此初始化一个会话的开销并不大
db_session = sessionmaker(bind=engine)
session = db_session()
BaseModel = declarative_base()


def init_db():
    # 创建表
    BaseModel.metadata.create_all(engine)


def drop_db():
    # 删除表
    BaseModel.metadata.drop_all(engine)


class User(BaseModel):
    __tablename__ = 't_user_info'
    user_id = Column('user_id', String(32), primary_key=True)
    user_pid = Column('user_pid', String(32))
    user_name = Column('user_name', String(32))
    com_id = Column('com_id', String(32))
    imei = Column('imei', String(32))
    phone_no = Column('phone_no', String(32))
    password = Column('password', String(32))
    user_sts = Column('user_sts', String(32))
    business_nature = Column('business_nature', String(32))


# 向数据库插入记录
# user=User(user_id='11000000',user_pid='00000000',user_name='哈哈'.decode('utf8'),com_id='11000000',imei=None,phone_no='13813813888',
#           password='123456',user_sts='1',business_nature='1')
# session.add(user)
# session.commit()

query = session.query(User)
# 显示执行SQL语句
# print query
# 显示执行SQL语句
# print query.statement
# 遍历时查询
# for i in query:
#     print i.user_id
# 返回的是一个类似列表的对象
# print query.all()
# 记录不存在时，first() 会返回 None
# print query.first().user_id
# 不存在，或有多行记录时会抛出异常
# print query.one('哈哈').user_name

# print query.filter(User.user_id == '10000000').first().user_name.decode('gbk')
# 等同于上一句，已主键获取
# print query.get('10000000').com_id

query2=session.query(User.user_id)
#每一行都是个元组
# print query2.all()
#最多返回1条记录
# print query2.limit(1).all()
# 从第 2 条记录开始返回
# print query2.offset(2).all()
#根据user_id进行排序--从小到大
# print query2.order_by(User.user_id).all()
#根据user_id进行排序--从大到小
# print query2.order_by(User.user_id.desc()).all()
# 如果有记录，返回第一条记录的第一个元素
# print query2.filter(User.user_id=='10000000').scalar()

# print session.query('user_id').select_from(User).filter(User.user_id=='10000000').scalar()
# print query.count()

User.user_id = 'dddddddd'
session.flush() # 写数据库，但并不提交
print query.filter(User.user_id == 'dddddddd')