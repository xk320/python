#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 多外键关联，并且关联同一个表。  下表中，Customer表有2个字段都关联了Address表   cat orm_many_fk.py
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    # 账单地址和邮寄地址 都关联同一个地址表
    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))
    def __repr__(self):
        return self.street

engine = create_engine("mysql+pymysql://root:123456@localhost/test",
                                    encoding='utf-8')
Base.metadata.create_all(engine)  # 创建表结构