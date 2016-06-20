# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
f = open('howzhihu.txt','w')     #打开文件
for pagenum in range(1,35):        #从第1页爬到第20页
    strpagenum = str(pagenum)      #页数的str表示
    print "Getting data for Page " + strpagenum   #shell里面显示的，表示已爬到多少页
    url = "http://www.zhihu.com/collection/27109279?page="+strpagenum  #网址
    page = urllib2.urlopen(url)     #打开网页
    soup = BeautifulSoup(page)      #用BeautifulSoup解析网页
    #找到具有class属性为下面两个的所有Tag
    ALL = soup.findAll(attrs = {'class' : ['zm-item-title','zh-summary summary clearfix'] })
    for each in ALL :               #枚举所有的问题和回答
        #print type(each.string)
        #print each.name
        if each.name == 'h2' :      #如果Tag为h2类型，说明是问题
            print each.a.string     #问题中还有一个<a..>，所以要each.a.string取出内容
            if each.a.string:       #如果非空，才能写入
                f.write(each.a.string)
            else :                  #否则写"No Answer"
                f.write("No Answer")
        else :                      #如果是回答，同样写入
            print each.string
            if each.string: 
                f.write(each.string)
            else :
                f.write("No Answer")
f.close()                           #关闭文件