# -*- coding=utf-8 -*-
__author__ = 'zhen'

import urllib
import urllib2


def post(url, data):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    #enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    return response.read()


def main():
    posturl = "http://wjw.sysu.edu.cn/"
    data = {  'username':'12353235', 'password':'01020010'}
    print post(posturl, data)


if __name__ == '__main__':
    main()
