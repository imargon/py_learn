#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import unicode_literals
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')

from pandas import DataFrame,Series
import numpy as np

import pandas as pd
import pylab
df_csv = pd.read_csv('d:/py/py_learn/numpy/train.csv',header=0)

#Series 就如同列表一样，一系列数据，每个数据对应一个索引值

s = Series([100,"python","Soochow","Qiwsir"])
print s,dir(s)
#index z指定索引
s2 = Series([100,"python","Soochow","Qiwsir"],index=["mark","title","uninversity","name"])

sd = {"python":8000,"c++":10990,"c#":10000}
sd1 = Series(sd)

df = {"name":["yahoo","google","facebook"], "marks":[200,400,800], "price":[9, 3, 7]}
df1 = DataFrame(df)
df2 = DataFrame(df,columns=['name','price','marks'])
df3 = DataFrame(df,columns=['name','price','marks','debt'],index=['a','b','c'])

# 字典套字典方式实现 dataframe

newdata = {"lang":{"firstline":"python","secondline":"java"}, "price":{"firstline":8000}}
df4= DataFrame(newdata,index=['a','b','c'])





print df_csv.head()
print df_csv.info()
print df_csv.describe()

print df_csv.Age[0:10]
print df_csv['Age'][0:10]

print df_csv.Age.mean()
print df_csv[['Sex','Pclass','Age']]
print df_csv[df_csv['Age']>60][['Sex','Pclass','Age','Survived']]

df_csv['Age'].hist()
pylab.show()

df_csv['Age'].dropna().hist(bins=16, range=(0,80), alpha = .5)
pylab.show()



for i in range(1,4):
    print i,len(df_csv[df_csv['Sex'] == 'male' & (df_csv['Pclass'] ==i) ] )

df_csv['Gender'] = 4
df_csv['Gender'] = df_csv['Sex'].map(lambda x:x[0].upper())
df_csv['Sex'] = df_csv['Sex'].map({'female':0,'male':1}).astype(int)


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
DataFrame(data, columns=['year', 'state', 'pop'])