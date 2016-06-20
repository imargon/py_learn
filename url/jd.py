#encoding:utf-8

#http://hackerxu.com/2014/09/07/scrapy-jd.html
import os,re,sys
import urllib,urlib2
def parse(self, response):
        '获取全部分类商品'
        req = []
        for sel in response.xpath('/html/body/div[5]/div[2]/a'):
            name = sel.xpath('text()').extract()
            href = sel.xpath('@href').extract()
            for i in href:
                if 'category' in i:
                    url = "http://wap.jd.com" + i
                    # print url
                    r = Request(url, callback=self.parse_category)
                    req.append(r)
        return req


#这个页面就是服饰内衣的页面了,我们抓取每个页面的蓝色字体的小分类,保存进req

def parse_category(self,response):
        '获取分类页'
        req = []
        for sel in response.xpath('/html/body/div[5]/div/a'):
            href = sel.xpath('@href').extract()
            for i in href:
                url = "http://wap.jd.com" + i
                # print url
                r = Request(url, callback=self.parse_list)
                req.append(r)
        return req
        
#这个就是列表页面了,我们沿着这个页面可以抓取所有商品的url,要说的就是要把下一页也放到parse_list里进行循环

def parse_list(self,response):
        '分别获得商品的地址和下一页地址'
        req = []

        '下一页地址'
        next_list = response.xpath('/html/body/div[21]/a[1]/@href').extract()
        if next_list:
            url = "http://wap.jd.com" + next_list[0]
            r = Request(url, callback=self.parse_list)
            req.append(r)

        '商品地址'
        for sel in response.xpath('/html/body/div[contains(@class, "pmc")]/div[1]/a'):
            href = sel.xpath('@href').extract()
            for i in href:
                url = "http://wap.jd.com" + i
                # print url
                r = Request(url, callback=self.parse_product)
                req.append(r)
        return req

#在这里抓取title,price和id,id就是 http://wap.jd.com/product/1268172347.html 最后的数字.

#把上面网址中的product改成comments,就可以抓取评论页了  

def parse_product(self,response):
        '商品页获取title,price,product_id'
        url = re.sub('product','comments',response.url)
        r = Request(url,callback=self.parse_comments)

        title = response.xpath('//title/text()').extract()[0][:-6]
        price = response.xpath('/html/body/div[4]/div[4]/font/text()').extract()[0]
        product_id = response.url.split('/')[-1][:-5]


        item = TutorialItem()
        item['title'] = title
        item['price'] = price
        item['product_id'] = product_id
        r.meta['item'] = item
        print title,price,product_id
        return r
#这个页面也没什么好说的,把好中差评论加一起就是商品总数了,然后返回item(如何爬取属性在不同页面的item呢？scrapy里面介绍的很详细了               

def parse_comments(self,response):
        '获取商品comment'
        comment_5 = response.xpath('/html/body/div[4]/div[2]/a[1]/font[2]/text()').extract()
        comment_3 = response.xpath('/html/body/div[4]/div[2]/a[2]/font/text()').extract()
        comment_1 = response.xpath('/html/body/div[4]/div[2]/a[3]/font/text()').extract()
        comment = comment_5 + comment_3 + comment_1
        print comment
        totle_comment = sum([int(i.strip()) for i in comment])
        item = response.meta['item']
        item['comment'] = totle_comment
        print totle_comment
        return item
