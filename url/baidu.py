#encoding:utf-8
__author__ = 'zhen'

import urllib.request
url="https://www.baidu.com/"
data = urllib.request.urlopen(url)
type(data)
data.geturl()
data.info()
data.getcode()
