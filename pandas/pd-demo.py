#https://www.pypandas.cn/docs/getting_started/10min.html#%E5%AF%B9%E8%B1%A1%E5%88%9B%E5%BB%BA
import numpy as np
import pandas as pd
s = pd.Series([1, 3, 5, np.nan, 6, 8])
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
 
