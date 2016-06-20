#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from __future__ import unicode_literals
import sys
import collections
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'zhen'

states = ('Rainy', 'Sunny')

observations = ('walk', 'shop', 'clean')

start_probability = {'Rainy': 0.6, 'Sunny': 0.4}

transition_probability = {
    'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6},
    }

emission_probability = {
    'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
}
if 'Rainy' in start_probability.keys():
    print start_probability.keys()

for (k, v) in start_probability.items():
    print k,v


# #关于 dct.get(key[, default]) ,如果 key 存在,返回 dct[key],否则返回 default
# dct[key] = dct.get(key,0) + 1
#
#
d = [1,2,2,3,4,1,1,3,7,89,9]
print Counter(d)
#
# #setdefault(key, default) 所做的是：
# # 如果存在，返回 dct[key] , 不存在则把 dct[key] 设为 default 并返回它。
# # 当一个默认的值是一个你可以修改的对象的时候这是很有用的。

group = []
for (key,value) in start_probability:
    group = start_probability.setdefault(key,[])
    group.append(value)
#print group.keys()
#
# dct = defaultdict(list)
# for (key,value) in data:
#     dct[key].append(value)


