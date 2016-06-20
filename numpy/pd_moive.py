#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import pandas as pd
unames =['user_id','gender','age','occupation','zip']
users = pd.read_table('D:/py/py_learn/ml-1m/users.dat',sep='::',header=None,names=unames, engine='python')

rnames =['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('D:/py/py_learn/ml-1m/ratings.dat',sep='::',header=None,names=rnames, engine='python')

mnames =['movie_id','title','genres']
movies = pd.read_table('D:/py/py_learn/ml-1m/movies.dat',sep='::',header=None,names=mnames, engine='python')

data = pd.merge(pd.merge(ratings,users),movies)

#以moive_id进行分组，计算occupation 的均值和合计
#index 分组(列名显示)，values计算均值与总计，columns:行名显示，类似于横转纵
mean_ratings = pd.pivot_table(data,index=["moive_id"],values=["occupation"],aggfunc=[pd.mean,pd.sum])

data = pd.read_csv('D:/py/py_learn/numpy/train.csv',header=0)

data2= data.groupby('title').size().sort_values()
data3 = data2.index[data2>= 250]
print data3


#行名显示为gender
print pd.pivot_table(data,index="title",values="rating",columns="gender",aggfunc='mean')

print data.sort()













#读取excel
#xls_data = pd.ExcelFile("D:\py\py_learn\ml-1m\emp_info.xlsx")
#print xls_data.parse("Sheet1")

#print mean_ratings.head()

