#encoding:utf-8
import requests
from requests import session

def login():
    cf = ConfigParser.ConfigParser()
    cf.read("config.ini")
    cookies = cf._sections['cookies']

    email = cf.get("info", "email")
    password = cf.get("info", "password")
    cookies = dict(cookies)
    global s
    s = requests.session()
    login_data = {"email": email, "password": password}
    header = {
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
    'Host': "www.zhihu.com",
    'Referer': "http://www.zhihu.com/",
    'X-Requested-With': "XMLHttpRequest"}
    r = s.post(Login_url, data=login_data, headers=header)