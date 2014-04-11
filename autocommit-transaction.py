#!/usr/bin/env python 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import sqlalchemy as sa

BASE = declarative_base()
engine = create_engine('postgres://postgres:postgres@dev1/test', echo=True)

maker = sessionmaker(bind=engine, autocommit=False)

class Users(BASE):
    """"""
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    email= sa.Column(sa.String)

user = Users()
user.name = 'abc'
user.email = 'abc@qunar.com'

print "session with autocommit=False"
session = maker()
print 'session.dd'
session.add(user)
print 'session.commit()'
session.commit()

print "-" * 78
user = Users()
user.name = 'abc'
user.email = 'abc@qunar.com'

autocommit_maker = sessionmaker(bind=engine, autocommit=True)
print "session with autocommit=True"
session = autocommit_maker()
print 'session.add'
with session.begin(subtransactions=True):
  session.add(user)
  session.flush()
  #raise Exception('error')
  print 'session.commit()'
  # session.commit()
