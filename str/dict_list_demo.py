#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#Python 中有三个非常好用的数据结构,列表,元组和字典, 元组是不可变的,
# 列表可以保存任意类型的Python对象,并可以随意扩展没有大小限制,
# 字典是一个key-value的键值映射的类型,可以存放任何Python对象,可以嵌套字典, 值可以是字典元组或者字典

info = {}
info1 = dict()

info = {"name":"cold"}
info1 = dict(name = 'warm')

info2 = dict.fromkeys(['name','blog'],'imargon')

info3 = {'name':'cold','blog':'github'}
info3['weather'] ='sunny'
info3['wet'] = 'rainy'
print info3.get('name')
print info.keys()

info3.update({'name':'cold day'})
del info3['name']

info3['name'] ='cold'
info3['blog'] ='github.com'

for key,value in info3.items():
    print key,':',value

#Python中所有对列表和字典的使用仅仅是对原来对象的引用而不是创建一个新的对象
names = ['cold', 'night', 'linuxzen']
names2 = names
names2.append('cold night')
print names
#['cold', 'night', 'linuxzen', 'cold night']
# copy 字典而不是list，同时list没有append方法


print names2
names3 = info3.copy()
names3.append('hot weather')
print names3