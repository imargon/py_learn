#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from __future__ import unicode_literals
import sys,os,string
import simplejson as  json

#reload(sys)
#sys.setdefaultencoding('utf-8')
#print sys.getdefaultencoding()
__author__ = 'zhen'

#编码：把一个Python对象编码转换成Json字符串 json.dumps()
#解码：把Json格式字符串解码转换成Python对象 json.loads()
#print os.listdir('d:/py/')
print os.getcwd()
json_file='D:/py/doubanmoive/dbmoive8.json'
with open(json_file,'r') as f:
    json_data = json.load(f,encoding='UTF-8')
    json_data = json.dumps(json_data,ensure_ascii=False,indent=1)
print type(json_data)
print json_data

#print json_data
ss=u'\u627e\u5de5\u4f5c-\u4e92\u8054\u7f51\u62db\u8058\u6c42\u804c\u7f51-\u62c9\u52fe\u7f51'
#ss = u'\u7f57\u9a6c\u5047\u65e5'
print ss.encode('utf-8')

#fp=open(json_file,'r')
#with open(json_file,'r') as f:
#    config = json.load(f,encoding='utf-8')
#print config

s = json.loads('{"name":"test","type":{"name":"seq","parameter": ["1","2"]}}')
print s
print s.keys()
print s["name"]
print s["type"]["parameter"]
print s["type"]["name"]

s2 = [{'a':"A",'b':(2,4),'c':3.0}]
print "s2 type:",type(s2)
print "s2",repr(s2)

s2_str = json.dumps(s2,indent=2)
print "s2_str:",s2_str
print "s2_str type:",type(s2_str)


data = {'a':123,'b':[1,2]}
di = json.dumps(data)
print type(data)

print type(di)
d2  = json.loads(di)
print d2
print type(d2)

data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
print json.dumps(data1,sort_keys=True,indent=4)
print json.dumps(data2)
print json.dumps(data2,sort_keys=True)
print json.dumps(data2,separators=(',',':'))
print len(repr(data1))
