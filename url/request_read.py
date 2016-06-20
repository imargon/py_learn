# -*- coding: utf-8 -*-
__author__ = 'zhen'

import urllib
import urllib2
import socket
import StringIO
import gzip
import nltk
import time
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8') #把 str 编码由 ascii 改为 utf8 (或 gb18030)


request = urllib2.Request('http://www.caixin.com/')
request.add_header('User-Agent','fake-client')
#response = urllib2.urlopen(request)

f = urllib2.urlopen(request,timeout=1)
isGzip = f.headers.get('Content-Encoding')
if isGzip:
    compressData = f.read()
    compressStream = StringIO.StringIO(compressData)
    gzipper = gzip.GzipFile(fileobj=compressStream)
    data = gzipper.read()
else:
    data = f.read()
    contentType = f.headers.get('Content-Type')
    if contentType.find("gbk"):
        data=data.decode('utf-8','ignore') #忽略非法字符
        #data = unicode(data,"gbk").encode("utf-8")
    elif contentType.find("utf-8"):
        pass

data = nltk.clean_html(data)
#clean_data = nltk.word_tokenize(data)
print data