#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import os,io
import time
import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


#num获取num页 国内高匿ip的网页中代理数据
def fetch_proxy(num):
    #修改当前工作文件夹
    os.chdir('D:/py/py_learn/proxy')
    api = 'http://www.xicidaili.com/nn/{}'
    header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    fp = io.open('host.txt', 'a+', encoding=('utf-8'))
    for i in range(num+1):
        api = api.format(1)
        respones = requests.get(url=api, headers=header)
        soup = BeautifulSoup(respones.text, 'lxml')
        container = soup.find_all(name='tr',attrs={'class':'odd'})
        for tag in container:
            try:
                con_soup = BeautifulSoup(str(tag),'lxml')
                td_list = con_soup.find_all('td')
                ip = str(td_list[1])[4:-5]
                port = str(td_list[2])[4:-5]
                IPport = ip + '\t' + port + '\n'
                fp.write(IPport)
            except Exception as e:
                print('No IP！')
        time.sleep(1)
    fp.close()


def test_proxy():
    N = 1
    os.chdir('D:/py/py_learn/proxy')
    url = 'https://www.baidu.com'
    fp = open('host.txt', 'r')
    ips = fp.readlines()
    proxys = list()
    for p in ips:
        ip = p.strip('\n').split('\t')
        proxy = 'http:\\' + ip[0] + ':' + ip[1]
        proxies = {'proxy': proxy}
        proxys.append(proxies)
    for pro in proxys:
        try:
            s = requests.get(url, proxies=pro)
            print('第{}个ip：{} 状态{}'.format(N,pro,s.status_code))
        except Exception as e:
            print(e)
        N+=1


def proxypool(num):
    n = 1
    os.chdir('D:/py/py_learn/proxy')
    fp = open('host.txt', 'r')
    proxys = list()
    ips = fp.readlines()
    while n<num:
        for p in ips:
            ip = p.strip('\n').split('\t')
            proxy = 'http:\\' + ip[0] + ':' + ip[1]
            proxies = {'proxy': proxy}
            proxys.append(proxies)
            n+=1
    return proxys


def run():
    print "hello"

if __name__ == "__main__":
    run()
    fetch_proxy(20)
    test_proxy()
    proxypool(20)