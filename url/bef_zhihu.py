# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
f = open('howzhihu.txt','w')     #���ļ�
for pagenum in range(1,35):        #�ӵ�1ҳ������20ҳ
    strpagenum = str(pagenum)      #ҳ����str��ʾ
    print "Getting data for Page " + strpagenum   #shell������ʾ�ģ���ʾ����������ҳ
    url = "http://www.zhihu.com/collection/27109279?page="+strpagenum  #��ַ
    page = urllib2.urlopen(url)     #����ҳ
    soup = BeautifulSoup(page)      #��BeautifulSoup������ҳ
    #�ҵ�����class����Ϊ��������������Tag
    ALL = soup.findAll(attrs = {'class' : ['zm-item-title','zh-summary summary clearfix'] })
    for each in ALL :               #ö�����е�����ͻش�
        #print type(each.string)
        #print each.name
        if each.name == 'h2' :      #���TagΪh2���ͣ�˵��������
            print each.a.string     #�����л���һ��<a..>������Ҫeach.a.stringȡ������
            if each.a.string:       #����ǿգ�����д��
                f.write(each.a.string)
            else :                  #����д"No Answer"
                f.write("No Answer")
        else :                      #����ǻش�ͬ��д��
            print each.string
            if each.string: 
                f.write(each.string)
            else :
                f.write("No Answer")
f.close()                           #�ر��ļ�