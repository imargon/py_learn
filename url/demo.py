#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import locale
import StringIO
import gzip
import urllib
from urllib import unwrap
import urllib2
import cookielib
import re

def read_data(resp):
    # 读取响应内容 如果是gzip类型则解压缩
    if result.info().get('Content-Encoding') == 'gzip':
        buf = StringIO.StringIO(resp.read())
        gzip_f = gzip.GzipFile(fileobj=buf)
        return gzip_f.read()
    else:
        return resp.read()

auth_url = 'http://www.sina.com/'
home_url = 'http://www.sina.com/'
# 登陆用户名和密码
data={
    "username":"nowamagic",
    "password":"pass"
}
# urllib进行编码
post_data=urllib.urlencode(data)
# 发送头信息
headers = {
    "Host":"www.sina.com",
    "Referer": "http://www.sina.com/",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36"
    "Gecko/20100101 Firefox/34.0",
    'Accept': "image/webp,*/*;q=0.8",
    'Accept-Language': "zh-CN,zh;q=0.8",
    'Accept-Encoding': "gzip, deflate, sdch"
}
# 初始化一个CookieJar来处理Cookie
cookieJar=cookielib.CookieJar()
# 实例化一个全局opener
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
# 获取cookie
req=urllib2.Request(auth_url,post_data,headers)

result = opener.open(req)
result=read_data(result)
# 访问主页 自动带着cookie信息
result = opener.open(home_url)
# 显示结果
print result.read()