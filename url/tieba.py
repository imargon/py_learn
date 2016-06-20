#-*-coding:utf-8 -*-
__author__ = 'zhen'
import urllib2
import re
import requests
from lxml import etree

links=[]
k=1
print u'请输入最后的页数：'
endPage=int(raw_input())
for j in range(0,endPage):
    url='http://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn='+str(j)
    html=urllib2.urlopen(url).read()
    selector = etree.HTML(html)
    links=selector.xpath('//div/a[@class="j_th_tit"]/@href')

for i in links:
    url1="http://tieba.baidu.com"+i
    html1=urllib2.urlopen(url1).read()
    selector=etree.HTML(html1)
    link=selector.xpath('//img[@class="DBF_Image"]/@src')

    for each in link:
        print u'正在下载%d'%k
        fp = open('image/'+str(k)+'.bmp','wb')
        image1=urllib2.urlopen(each).read()
        fp.write(image1)
        fp.close()
        k+=1

print u'下载完成'

































