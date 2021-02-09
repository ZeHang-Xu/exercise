import pandas as pd
import numpy as np

# data = pd.DataFrame({'A': [1, 1, 2, 2], 'B': ['a', 'b', 'a', 'b']})
# print(data)
#
# # DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
# # subset用来指定默认的列，默认所有列
# # keep: {'first', 'last', False}, default 'first' 删除重复并保留第一次出现的元素
# # inplace : boolean, default False 可以选择要在原来的数据上修改还是保留一个副本
# data.drop_duplicates(subset='B', keep='first', inplace=True)
# print(data)


# df.isin 确认每个元素和所查询的值是否有重复
# df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'f']})
# print(df.isin([1, 3, 12, 'a']))
# print(df.isin({'A': [1, 3], 'B': ['b', 'f', 'g']}))
# other = pd.DataFrame({'A': [1, 3, 3, 2], 'B': ['e', 'f', 'f', 'e']})
# print(df.isin(other))   # 如果是DataFrame做比对，则保持相同的列

# ipl_data = {
#     'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'Kings',
#              'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#     'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
#     'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
#     'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]
# }

# df = pd. DataFrame(ipl_data)
# print(df)
# grouped = df.groupby('Team')
# print(grouped)
# print(grouped.groups)
# print(df.groupby(['Team', 'Year']).groups)

# grouped = df.groupby('Year')
# print(grouped)
# for year, data in grouped:
#     print(year, data, sep=':\n', end='\n----------------------------------\n')

# print(grouped.get_group(2014))

# 相同年份的分数相加取平均值
# print(grouped['Points'].mean())
# print(grouped['Points'].agg(np.mean))
# grouped = df.groupby('Team')
# print(grouped['Points'].agg([np.mean, np.sum, np.std]))

# df = pd. DataFrame({
#     'A': [1, 1, 2, 2, 2],
#     'B': [1, 2, 3, 4, 4],
#     'C': np.random.randn(5)
# })
# print(df)
# print(df.groupby('A').agg('min'))  # 'mean'、'sum'、'max'

# df = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'], index=pd.date_range('1/1/2020', periods=10))
# # print(df)
# df.iloc[3:7] = np.nan
# print(df)
# print(df.agg('sum'))
# print(df.agg([sum, min]))
# print(df.agg({'A': ['sum', 'min'], 'B': ['min', 'max']}))

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)
})
# grouped = df.groupby(['A', 'B'], as_index=False)  # index 高度一致
# print(grouped['C'].sum())
# print(grouped.agg(sum))
# print(grouped.min())
# print(grouped.agg(np.sum))
# print(grouped.agg(sum))
# print(grouped.sum())

# for x, y in grouped:
#     print(x)
#     print(y)
#     print('----------------------------------------------')

# print(df.groupby(['A', 'B']).sum())
# print(df.groupby(['A', 'B']).sum().reset_index())
# print(grouped.size())

grouped = df.groupby('A')

print(grouped['C'].agg([np.sum]))
print(grouped['C'].agg(sum))


df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])
# print(df)
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# print(df['one'].isna())
print(df['one'].sum())
