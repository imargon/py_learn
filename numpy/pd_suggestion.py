#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import sys

data = pd.read_csv('D:/py/py_learn/numpy/train.csv',header=0)
print data.head()
#data.loc[(data["Sex"]=="female")&(data["Age"]>25)&(data["SibSp"]=="1"),["Sex","Age","SibSp"]]
print data[data['Age']>25]