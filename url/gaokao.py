#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'holmes'

from HTMLParser import HTMLParser
import urllib2
import StringIO, gzip
import threading
import os
import time
import sys
import socket


schoollist = ['1','2','3']
# hard code
LOCATION = ("北京", "天津", "辽宁", "吉林", "黑龙江", "上海", "江苏", "浙江", "安徽", "福建", "山东", "湖北",
            "湖南", "广东", "重庆", "四川", "陕西", "甘肃", "河北", "山西", "内蒙古", "河南", "海南", "广西",
            "贵州", "云南", "西藏", "青海", "宁夏", "新疆", "江西",)
# hard code
SUBJECT = ("理科", "文科",)
'''Rules for URL
http://college.gaokao.com/school/tinfo/%d/result/%d/%d/ %(schoolID,localID,subID)
where localID from 1 to 31
where subID from 1 to 2
'''
SEED = "http://college.gaokao.com/school/tinfo/%s/result/%s/%s/"

SID = "schoolID"  # file name contains school IDs


class SpiderParser(HTMLParser):
    def __init__(self, subject=1, location=1):
        HTMLParser.__init__(self)
        self.campus_name = ""
        self.subject = SUBJECT[subject - 1]
        self.location = LOCATION[location - 1]
        self.table_content = [[], ]
        self.line_no = 0

        self.__in_h2 = False
        self.__in_table = False
        self.__in_td = False

    def handle_starttag(self, tag, attrs):
        if tag == "h2":
            self.__in_h2 = True
        if tag == "table":
            self.__in_table = True

        if tag == "tr" and len(attrs) != 0:
            if self.__in_table:
                self.table_content[self.line_no].append(self.campus_name)
                self.table_content[self.line_no].append(self.subject)
                self.table_content[self.line_no].append(self.location)

        if tag == "td":
            if self.__in_table:
                self.__in_td = True

    def handle_endtag(self, tag):
        if tag == "h2":
            self.__in_h2 = False
        if tag == "table":
            self.__in_table = False
        if tag == "tr":
            if self.__in_table:
                self.line_no += 1
                self.table_content.append([])
        if tag == "td":
            if self.__in_table:
                self.__in_td = False

    def handle_data(self, data):
        if self.__in_h2:
            self.campus_name = data
        if self.__in_td:
            self.table_content[self.line_no].append(data)


def getschoolID():
    with open(SID, mode='r') as rf:
        idlist = rf.readlines()
        print idlist
        return idlist


def gethtml(url):
    try:
        f = urllib2.urlopen(url,timeout=10)
    # consider some html is compressed by server with gzip
        isGzip = f.headers.get('Content-Encoding')
        if isGzip:
            compressedData = f.read()
            compressedStream = StringIO.StringIO(compressedData)
            gzipper = gzip.GzipFile(fileobj=compressedStream)
            data = gzipper.read()
        else:
            data = f.read()
    # decode the html
        contentType = f.headers.get('Content-Type')
        if contentType.find("gbk"):
            data = unicode(data, "GBK").encode("utf-8")
        elif contentType.find("utf-8"):
            pass
    except socket.timeout, e:
        data = None
        print "time out!"
        with open("timeout",'a') as log:
            log.write(url+'\n')
    finally:
        return data


def parseandwrite((slID, lID, sID), wfile):
    try:
        url = SEED % (slID, lID, sID)
        html = gethtml(url)
        if html is None:
            print "pass a timeout"
            return
        parser = SpiderParser(sID, lID)
        parser.feed(html)
        parser.close()
        if parser.line_no != 0:
            for line in parser.table_content:
                for item in line:
                    if "--" in item:
                        item = "NULL"
                    wfile.write(item + ',')
                wfile.write('\n')
    except urllib2.URLError, e:
        print "url error in parseandwrite()"
        raise


def thread_task(idlist, name):
    try:
        print "thread %s is start" % name
        wf = open(name, mode='w')
        wf.write("大学名称,文理,省份,年份,最低分,最高分,平均分,录取人数,录取批次")
        for sID in idlist:
            print name + ":%s" % idlist.index(sID)
            sID = sID.strip('\n')
            i = 1.0
            for localID in range(1, 32):
                for subID in range(1, 3):
                    parseandwrite((sID, localID, subID), wf)
                    sys.stdout.write("\rprocess:%.2f%%" % (i / 62.0 * 100))
                    sys.stdout.flush()
                    i += 1.0
                    time.sleep(1)
    except urllib2.URLError:
        with open("errorlog_" + name, 'w') as f:
            f.write("schoolID is %s , locationID is %s ,subID is %s" % (sID, localID, subID))
        print "schoolID is %s ,locationID is %s ,subID is %s" % (sID, localID, subID)
    finally:
        wf.close()


THREAD_NO = 1


def master():
    school = getschoolID()
    for i in range(THREAD_NO):
        path = os.path.join(os.path.curdir, "errorlog_" + str(i))
        if os.path.exists(path):
            with open("errorlog_" + str(i), 'r') as rf:
                sID = rf.readline().split()[2]
                start = school.index(sID)
        else:
            start = len(school) / THREAD_NO * i
        end = len(school) / THREAD_NO * (i + 1) - 1
        if i == THREAD_NO - 1:
            end = len(school) - 1
        t = threading.Thread(target=thread_task, args=(school[start:end], "thread" + str(i),))
        t.start()
        print "start:%s \n end:%s" % (start, end)
    t.join()

    print "finish"


if __name__ == '__main__':
    # thread_task(["1"],"test")
    master()
    # gethtml("http://www.baidu.com")
