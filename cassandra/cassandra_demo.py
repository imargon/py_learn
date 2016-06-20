#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pip install cassandra-driver

from __future__ import unicode_literals
import sys
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy


reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'zhen'

cluster = Cluster()
session = cluster.connect('photos') # connect to database

#session.execute('INSERT INTO users(name, age, email) VALUES(%s, %s, %s)', ('shawn', 21, 'shawn@163.com'))

rows = session.execute('select user_id,email,uname from cqlusers')
for(user_id,email,uname) in rows:
    print user_id,email,uname