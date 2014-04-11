#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import sqlalchemy as sa
import time

BASE = declarative_base()
ENGINE = create_engine('postgresql://postgres:postgres@192.168.122.10/test', echo=False)

class Users(BASE):
    """"""
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    email= sa.Column(sa.String)

maker = sessionmaker(bind=ENGINE)
sessions = []
for count in range(0, 10):
    session = maker(autocommit=False)
    session.query(Users).all()
    sessions.append(session)
    rows = ENGINE.execute('SELECT current_query FROM pg_stat_activity');
    # session.commit()
    print "#connections =", len(list(rows))
    time.sleep(1)
