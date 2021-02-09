# 清理和整理missing data
# df.fillna() 括号内代表要补的值
import numpy as np
import pandas as pd

# df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'], columns=['one', 'two', 'three'])
# df = df.reindex(['a', 'b', 'c', 'd', 'e'])
# print(df)
# print(dffillna('han_han'))


# missing data 的补值
# pad/ffill --> follow前一项的资料补值
# bfill/backfill -> follow后一项的资料补值
# print(df.fillna(method='pad'))
# print(df.fillna(method='bfill'))
# print(df.dropna())
# print(df.dropna(axis=0))


df = pd.DataFrame({'one': [10, 20, 30, 40, 50, 20000], 'two': [1000, 0, 30, 40, 50, 60]})
print(df)
# print(df.replace([1000, 20000], [10, 60]))
print(df.replace({1000: 10, 20000: 60}))
