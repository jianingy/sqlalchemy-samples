#!/usr/bin/env python 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import sqlalchemy as sa
import time

BASE = declarative_base()
ENGINE = create_engine('postgresql://postgres:postgres@192.168.122.10/test', echo=True)

class Users(BASE):
    """"""
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    email= sa.Column(sa.String)


def show_pg_stat_activity():
  import os
  os.system("psql -c \"SELECT current_query, waiting, backend_start"
            " FROM pg_stat_activity"
            " WHERE client_addr='192.168.122.1'"
            " AND application_name != 'psql'\"")
  raw_input('Press enter to continue ...')

print '-' * 78
print 'run test: session with autocommit=False without commit.'
print '-' * 78
maker = sessionmaker(bind=ENGINE, autocommit=False)
session = maker()
print " --== session is", id(session), "==--"
result = session.query(Users).all()
show_pg_stat_activity()
session.close()

print '-' * 78
print 'run test: session with autocommit=False with commit.'
print '-' * 78
maker = sessionmaker(bind=ENGINE, autocommit=False)
session = maker()
print " --== session is", id(session), "==--"
result = session.query(Users).all()
session.commit()
show_pg_stat_activity()
session.close()

print '-' * 78
print 'run test: session with autocommit=True without commit.'
print '-' * 78
maker = sessionmaker(bind=ENGINE, autocommit=True)
session = maker()
print " --== session is", id(session), "==--"
result = session.query(Users).all()
show_pg_stat_activity()
session.close()

print '-' * 78
print 'run test: session with autocommit=True with commit.'
print '-' * 78
maker = sessionmaker(bind=ENGINE, autocommit=True)
session = maker()
print " --== session is", id(session), "==--"
result = session.query(Users).all()
session.commit()
show_pg_stat_activity()
session.close()





