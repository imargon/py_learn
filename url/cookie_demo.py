#encoding:utf-8
__author__ = 'zhen'

import urllib
import urllib2
import cookielib
import StringIO
import os
import sys

#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#创建一个请求，原理同urllib2的urlopen
response = opener.open("https://www.baidu.com")
#保存cookie到文件
postdata = urllib.urlencode({'stuid':'201200131012','pwd':'23342321'})
cookie.save(ignore_discard=True, ignore_expires=True)

for  item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value

a = open('cookie.txt','r')
print a.read()






