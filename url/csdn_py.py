# coding: utf-8
# """获取csdn博客类别列表"""
__author__ = 'zhen'
import urllib2
import gzip
import StringIO
import re
from urllib2 import URLError, HTTPError


def read_data(resp):
    # 读取响应内容 如果是gzip类型则解压缩
    if response.info().get('Content-Encoding') == 'gzip':
        buf = StringIO.StringIO(resp.read())
        gzip_f = gzip.GzipFile(fileobj=buf)
        return gzip_f.read()
    else:
        return resp.read()

URL = 'http://blog.csdn.net/'
HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36"
    "Gecko/20100101 Firefox/34.0"
    ,'Accept': "image/webp,*/*;q=0.8"
    , 'Accept-Language': "zh-CN,zh;q=0.8"
    , 'Accept-Encoding': "gzip, deflate, sdch"
}
req = urllib2.Request(URL, None, HEADERS)  # 通过添加头来达到伪装目的
try:
    response = urllib2.urlopen(req)
    page_content = read_data(response)
    encoding = response.headers['content-type'].split('charset=')[-1]
    p = re.compile(ur'(<a.*?href=)(.*?category.*?>)(.*)(</a>)')  # 解析类别的正则表达式
    m = p.findall(page_content.decode(encoding))
    if m:
        for x in m:
            print x[2].encode(encoding)
except URLError, e:
        if hasattr(e, 'code'):
            print '错误码: ', e.code, ',无法完成请求.'
        elif hasattr(e, 'reason'):
            print '请求失败: ', e.reason, '无法连接服务器'
else:
    print '请求已完成.'
