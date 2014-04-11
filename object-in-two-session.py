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

maker = sessionmaker(bind=ENGINE)
sessions = [maker(), maker()]
print "Sessions: ", map(lambda x: id(x), sessions)
user = Users()
user.name = 'user'
sessions[0].add(user)
sessions[1].add(user)
