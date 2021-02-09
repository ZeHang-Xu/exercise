import numpy as np
import pandas as pd

# data = np.array(['a', 'b', 'c', 'd'])
# s = pd.Series(data, index=['100', 101, 102, 103])
# print(s)
# print(s[0:3])

# df = pd.DataFrame(data)
# print(df)

# data = {'Name': ['Tom', 'Jerry', 'Steve', 'Rick'],
#         'Age': [32, 12, 54, 54]}
# df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
# print(df)

# data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 10, 'c': 20}]
# data = {'a': [1, 3], 'b': [2, 10], 'c': [None, 20]}
# df = pd.DataFrame(data)
# print(df)

# d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(d)
# # print(df['one'])
# df['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# df.pop('three')
# print(df)
# # print(df.loc['b'])
# print(df.iloc[2])

# df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
# df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
# df = df.append(df2)
# df = df.drop(0)
# print(df)

# unsorted_df = pd.DataFrame(np.random.randn(10, 2),
#                            index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
#                            columns=['cell1', 'cell2'])
# print(unsorted_df)
# sorted_df = unsorted_df.sort_index(ascending=False)
# sorted_df = unsorted_df.sort_index(axis=1)
# sorted_df = unsorted_df.sort_values(by='cell1')
# print(sorted_df)

# unsorted_df = pd.DataFrame({'cell1': [2, 1, 1, 1], 'cell2': [1, 2, 3, 4]})
# sorted_df = unsorted_df.sort_values(by='cell1', kind='mergesort')
# print(sorted_df)

# df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
# print(df.iloc[:4])
# print(df.iloc[1:5, 2:4])
# print(df.iloc[[1, 3, 5], [1, 3]])


# write json file
df = pd.DataFrame(np.random.randn(3, 3), columns=['A', 'B', 'C'])
json = df.to_json('data_cleaned.json', orient='records')
# read json file
df_read = pd.read_json('data_cleaned.json')
# 因为json档案中的资料内容有很多种，因此可以用orient去指定
# 可指定的形式有【split, records, index, columns, values】
# 同样Excel 和 Csv一样
