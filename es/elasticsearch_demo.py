import elasticsearch
import pyes
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

conn = pyes.ES('127.0.0.1:9200')
conn.create_index("hunman")
#human 是一个新的索引库，相当于create database操作
mapping = {'firstname':{'index':'analyzed',#使用分词器
                        'type':'string',
                        'analyzer':'ik' #分词器为ik
                        },
           'lastname':{'index':'not_analyzed','type':'string'},#不使用分词器
                'age':{'index':'not_analyzed','type':'long'}
           }
conn.put_mapping("man",{'properties':mapping},["human"]) #在human库中创建man，相当于create table操作
conn.put_mapping("woman",{'properties':mapping},["human"])
conn.index({'firstname':'David','lastname':'White','age':18},'human','man','David White',True) #向human的man中添加索引数据，相当于insert into操作
conn.index({'firstname':'Uni', 'lastname':'Lavender','age':18}, 'human', 'man', 'Uni Lavender', True)
conn.index({'firstname':'Jann', 'lastname':'White', 'age':18}, 'human', 'woman', 'Jann White', True)
conn.index({'firstname':'Suzan', 'lastname':'White','age':18}, 'human', 'woman', 'Suzan White', True)