# 等同于SQL的join
# pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
# left_index=False, right_index=False, sort=True)

# import numpy as np
import pandas as pd

left = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'AAA'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5']
})
right = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Name': ['Billy', 'Brain', 'Bran', 'Bryce', 'Bett'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5']
})
# # left join
# print(pd.merge(left, right, on='subject_id', how='left'))
# # right join
# print(pd.merge(left, right, on='subject_id', how='right'))

# # outer join (并集)
# print(pd.merge(left, right, how='outer', on='subject_id'))
# # inner join (交集)
# print(pd.merge(left, right, on='subject_id', how='inner'))

# # merging two df on a key
# print(pd.merge(left, right, on='id'))
# # merging two df on multi keys
# print(pd.merge(left, right, on=['id', 'subject_id']))


# # 另一种DataFrame的合并指令
# # pd.contact(objs, axis=0, join='outer', join_axis=None, ignore_index=False)
one = pd.DataFrame({
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5'],
    'Marks_scored': [98, 90, 87, 69, 78]},
    index=[1, 2, 3, 4, 5])

two = pd.DataFrame({
    'Name': ['Billy', 'Brain', 'Bran', 'Bryce', 'Betty'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5'],
    'Marks_scored': [89, 80, 79, 97, 88]},
    index=[1, 2, 3, 4, 5])
# # 合并两个DataFame
# print(pd.concat([one, two]))
# # 合并两个DataFrame分成x, y两个资料表
# print(pd.concat([one, two], keys=['x', 'y']))
# # 自动生成新的index合并两个df
# print(pd.concat([one, two], keys=['x', 'y'], ignore_index=True))

# # 横向合并
# # If two objects need to be added along axis=1, then the new columns will be appended.
# print(pd.concat([one, two], axis=1))


# # 利用append指令合并
# print(one.append(two))
print(one.append([two, one, two]))
