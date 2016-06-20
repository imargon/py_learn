#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import urllib2
import gzip,os

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'zhen'

#在一个较长的字符串中查询子字符串，返回子串所在位置最左端索引，没有找到返回-1
def url_open(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2498.0 Safari/537.36')
    response = urllib2.urlopen(req)
    html = response.read().decode('utf-8')
    a=html.find('current_page')+22
    b=html.find(']',a)
    #print html
    print "**************************"
    img_addrs=[]
    c=html.find('img src=')
    while c!=-1:
        d=html.find('.jpg',c,c+80)
        if d!=-1:
            img_addrs.append(html[c+9:d+4])
        else:
            d=c+9
            d=html.find('img src=',c)
    img_file=open('img_addrs.txt','w+')
    img_file.write(img_addrs)
    img_file.close()
    #return html

if __name__ == '__main__':
    url_open('http://jandan.net/ooxx/')

