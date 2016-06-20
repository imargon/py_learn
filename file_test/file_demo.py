#encoding:utf-8
__author__ = 'zhen'
import os,sys
import chardet

reload(sys)
sys.setdefaultencoding('utf-8')

path = 'C:\Users\zhen\Downloads'
file_iter = os.walk(path)
for x in file_iter:
    codedect = chardet.detect(x)
    x = unicode(x,codedect)
    x.encode("utf-8")
    #x = x.decode('utf-8')
    print x #x.encode('utf-8')

print "中国"