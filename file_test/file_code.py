#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import urllib,urllib2,chardet

__author__ = 'zhen'
def run():
    print "hello"

if __name__ == "__main__":
    run()

str= '这个剑神重生'

print str.decode('GBK').encode('UTF-8')

#td = urllib.urlopen('https://www.baidu.com/').read()
#print  chardet.detect(td)







