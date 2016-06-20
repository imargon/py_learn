#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys,re,os,string
import ConfigParser

reload(sys)
sys.setdefaultencoding('utf-8')
confile="D:/py/url/test.conf"

#解析字符串，防止出现乱码,因此解析之前，先替换掉
content = open('test.conf').read()
content = re.sub(r"\xfe\xff","",content)
content = re.sub(r"\xff\xfe","",content)
content = re.sub(r"\xef\xbb\xbf","",content)
open('test.conf','w').write(content)

parse = ConfigParser.ConfigParser()
parse.read('test.conf')

sections = parse.sections()
for i in sections:
    options = parse.options(i)
    values = parse.items(i)
    print "Section is %s " % i
    print "Options are %s " % options
    print "Values are %s " % values

print '_'*60

def read_config_file(filename):
    data = {}
    config = ConfigParser.ConfigParser()
    try:
        with open(filename,'r') as confile:
            config.readfp(confile)
            for i in config.sections():
                for (key,value) in config.items(i):
                    data[key] = value
                return data
    except Exception:
        print "Open file error."

    p = read_config_file(confile)
