#encoding:utf-8
import ConfigParser
import string,os,sys,re

#解析字符串，防止出现乱码
content = open('test.conf').read()
content = re.sub(r"\xfe\xff","",content)
content = re.sub(r"\xff\xfe","",content)
content = re.sub(r"\xef\xbb\xbf","",content)
open('test.conf','w').write(content)


cf =ConfigParser.ConfigParser()
cf.read("test.conf")
# 返回所有的section
#获取所有sections。也就是将配置文件中所有“[ ]”读取到列表中：
s=cf.sections()
print 'section:',s

#获取指定section 的options。即将配置文件某个section 内key 读取到列表中：
o = cf.options("db")
print 'options:',o

#获取指定section 的配置信息。
v = cf.items("db")
print 'db:',v
print '_'*60


#按照类型读出来
db_host = cf.get("db","db_host")
db_port = cf.get("db","db_port")
db_user = cf.get("db","db_user")
db_pass = cf.get("db","db_pass")

threads = cf.getint("concurrent","thread")
processors = cf.getint("concurrent","processor")

print "db_host:",db_host
print "db_port:", db_port
print "db_user:", db_user
print "db_pass:", db_pass
print "thread:", threads
print "processor:", processors

#修改一个值，再写回去
cf.set("db", "db_pass", "zhaowei")
cf.write(open("test.conf", "w"))


