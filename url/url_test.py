#encoding:utf-8
__author__ = 'zhen'

import urllib
import urllib2
import socket
import StringIO
import gzip
import time


def gethtml(url):
    try:
        f = urllib2.urlopen(url,timeout=10)
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
            data = unicode(data,"GBK").encode("utf-8")
        elif contentType.find("utf-8"):
            pass

    except socket.timeout,e:
        data = None
        print "time out"
        with open("timeout",'a') as log:
            log.write(url+'\n')
    except urllib2.URLError,ee:
        data = None
        print "url error"
    finally:
        return data

gethtml("http://www.cnbeta.com/")