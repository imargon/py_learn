#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.ituring.com.cn/article/114407

from __future__ import unicode_literals
import sys
import urllib2
import re
reload(sys)
sys.setdefaultencoding('utf-8')

# urls = "http://news.upc.edu.cn/sdyw/List_1.shtml"
# 固定字符串<a href="/sdyw/后跟了一个用括号包起来的字符串(?P<Date>.{10})，(?P<name>...) 是定义一个命名组，(?P=name)则是对命名组的逆向引用。
# 而后面的.匹配任意除换行符"\n"以外的字符。
# .{10}匹配10个任意字符，<a href="/sdyw/(?P<Date>.{10}).*的意思也就很清楚了，是将/sdyw/后面的10个字符命名为Date，后面的Title也是同样的道理。
# 列表推导式 for 必须写后面！！

for url in ["http://news.upc.edu.cn/sdyw/List_"+str(i)+".shtml" for i in range(1, 20)]:
    response = urllib2.urlopen(url)
    html = response.read()
    r = re.compile(r'<a href="/sdyw/(?P<Date>.{10}).*" target="_blank">(?P<Title>.+)</a>')
    news = r.findall(html)  # 将在html中所有匹配的字符串以列表的形式返回
    for i in range(len(news)):
        date = news[i][0]
        title = news[i][1]
        print title+" "+date
