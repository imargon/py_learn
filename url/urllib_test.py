#encoding:utf-8
__author__ = 'zhen'
import urllib2
import cookielib
import Cookie
import urllib


enable_proxy=True
proxy_support = urllib2.ProxyHandler({'http':'http://202.106.16.36:3128'})
cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
opener = urllib2.build_opener(proxy_support,cookie_support,urllib2.HTTPHandler)


urllib2.install_opener(opener)
content = urllib2.urlopen('http://www.caixin.com').read()
print content




