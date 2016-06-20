#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import os
import sys
import pyes

reload(sys)
sys.setdefaultencoding('utf-8')

#conn = pyes.ES('127.0.0.1:9200')

es = Elasticsearch([{'host':'10.3.34.54','port':9200}])

if es:
    print('conn es successful!')
else:
    print('conn es failed')
#conn.create_index("myindex",)
# 插入数据
es.index(index="myindex",doc_type="mytype",id=100,body={"name":"Peter","age":24})
es.index(index="myindex",doc_type="mytype",id=101,body={"name":"Margon","age":26})
es.index(index="myindex",doc_type="mytype",id=102,body={"name":"彭朕","age":27})
es.index(index="myindex",doc_type="mytype",id=103,body={"name":"dargon","age":27})    
#在末尾加上['_source']可以只显示结果
print es.get(index="myindex",doc_type="mytype",id=100)['_source']
# 查询age在10~100内的员工
es.search(index="myindex",doc_type="mytype",body={'query':{'range':{'age':{'from':10,'to':100}}}})
es.search(index="myindex",doc_type="mytype",body={'query':{'match':{'name':'Peter'}}})
es.search(index="myindex",doc_type="mytype",body={'query':{'match':{'name':'dargon'}}})
    
#删除索引，指定id
es.delete(index="myindex",doc_type="mytype",id=103)

#批量插入数据

j=0
actions =[]
while (j <=10000):
    action={
    "_index":"tickets_index",
    "_type":"tickets",
    "_id":j,
    "_source":{
    "any":"data"+str(j),
    "timestamp":datetime.now()
        }
    }
    actions.append(action)
    j+=1
    

#
helpers.bulk(es, actions)
