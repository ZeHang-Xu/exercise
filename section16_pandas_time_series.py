import numpy as np
import pandas as pd

# # create current timestamp
# print(pd.datetime.now())
# # create a timestamp
# print(pd.Timestamp('2018-06-06'))
# print(pd.Timestamp(1587687255, unit='s'))


# # create a range of time(30min)
# print(pd.date_range("11:00", "13:30", freq="30min"))
# print(pd.date_range("11:00", "13:30", freq="30min").time)
# print(pd.date_range("11:00", "13:30", freq="H").time)

# print(pd.to_datetime(pd.Series(['2017-01-01', '2018-01-10', None])))
# print('-----------------------------------------------------------')
# print(pd.to_datetime(['2017-01-01', '2018-01-11', None]))

# print(pd.date_range('1/1/2011', periods=5))
# print(pd.date_range('1/1/2011', periods=5, freq='M'))

# start = pd.datetime(2011, 1, 1)
# end = pd.datetime(2011, 1, 5)
# print(pd.date_range(start, end, freq='H'))

# # 时间格式的datafame操作
# s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
# td = pd.Series(pd.Timedelta(days=i) for i in range(3))
# df = pd.DataFrame(dict(A=s, B=td))
# print(df)

# # add operation C的日期等于A的日期加B的天数
# df['C'] = df['A'] + df['B']
# print(df)


import matplotlib as plt
# %matplotlib line

# df = pd.DataFrame(np.random.randn(10, 4), index=pd.date_range(1/1/2017, periods=10), columns=['a', 'b', 'c', 'd'])
# print(df)
# print(df.plot())

df = pd.DataFrame(np.random.randn(5, 5), columns=['a', 'b', 'c', 'd', 'e'])
# print(df.plot())
# print(df.plot.bar())
print(df.plot.bar(stacked=True))
print(df.plot.barh())
print(df.plot.barh(stacked=True))
