#coding:utf-8
#import urllib.request
import urllib2
import os

def url_open(url):
    req=urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2498.0 Safari/537.36')
    response=urllib2.urlopen(req)
    html=response.read()
    return html

#get page number
def get_page(url):
    html=url_open(url).decode('utf-8')
    a=html.find('current-comment-page')+23
    b=html.find(']',a)
    return html[a:b]

def find_imgs(url):
    html=url_open(url).decode('utf-8')
    img_addrs=[]
    a=html.find('img src=')
    while a!=-1:
        b=html.find('.jpg',a,a+80)
        if b!=-1:
            img_addrs.append(html[a+9:b+4])
        else:
            b=a+9
            a=html.find('img src=',b)
    return img_addrs


def save_imgs(folder,img_addrs):
    for img in img_addrs:
        filename=each.split('/')[-1]
        with open(filename,'wb') as f:
            img=url_open(img)
        f.write(img)
    
def download_MM(folder='OOXX',pages=20):
    proxy_handler=urllib2.ProxyHandler({'http':'219.139.291.125'})
    opener=urllib2.build_opener(proxy_handler)
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2498.0 Safari/537.36')]
    urllib2.install_opener(opener)
    os.mkdir(folder)
    os.chdir(folder)
    url='http://jandan.net/ooxx/'
    page_num=int(get_page(url))
    for i in range(pages):
         page_num-=i
         #make proper url
         page_url=url+'page-'+str(page_num)+'#comments'
         img_addrs=find_imgs(page_url)
         save_imgs(folder,img_addrs)

if __name__=='__main__':
    download_MM(folder='OOXX',pages=20)