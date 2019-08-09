#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd

file_path = 'F:/py/list.xlsx'


def read_file(file_path):
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    df = df.groupby('Official level')['amount'].sum()
    #file_dat = df.head()  # 默认读取前5行的数据
    print("获取到所有的值:\n{0}".format(df))  # 格式化输出


if __name__ == '__main__':
    read_file(file_path)
