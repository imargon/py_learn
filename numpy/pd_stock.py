#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from __future__ import unicode_literals

import pandas
from  pandas.io import data
import matplotlib.pyplot as plt

#from pandas_datareader import data, wb
import sys

# 阿里股票
sym = "BABA"
finace = pandas.io.data.DataReader(sym,data_source="yahoo",start="2014/11/01")
plt.plot(finace.index,finace["Open"])
print finace.head(3)
plt.show()
