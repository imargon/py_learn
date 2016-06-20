#coding:utf-8
import os
import urllib
url = "https://www.baidu.com"

def use_urllib():
    import urllib, httplib
    httplib.HTTPConnection.debuglevel = 1
    page = urllib.urlopen(url)
    print "status:", page.getcode() #200请求成功,404
    print "url:", page.geturl()
    print "head_info:\n",  page.info()
    print "Content len:", len(page.read())