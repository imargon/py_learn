#coding:utf-8
__author__ = 'zhen'

import urllib2
import StringIO
from StringIO import StringIO
import gzip

request = urllib2.Request('http://www.sina.com.cn/')
request.add_header('Accept-encoding', 'gzip')
response = urllib2.urlopen(request)
if response.info().get('Content-Encoding') == 'gzip':
    buf = StringIO( response.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
print data

