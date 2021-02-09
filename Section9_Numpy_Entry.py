import numpy as np
# from math import pi
# import pandas as pd


# a = np.linspace(0, 2*pi, 100)
# print(a)

# a = np.arange(8)
# a = a.reshape(2, 4)
# print(a)

# a = np.arange(2, 8, 2)
# print(a)

a = np.random.random((2, 3))
print(a)

# 针对不同的轴做简易的数学统计(譬如X轴Y轴, axis=1代表row, axis代表column)
# 如果不指定轴axis的值，代表在该空间所有元素中做统计处理
# a = np.arange(8).reshape(2, 4)
# print(a)
# print(a.mean(axis=1))  # 取平均值
# print(a.sum(axis=1))
# print(a.min(axis=1))
# print(a.max(axis=1))
# print(a.std(axis=1))  # 标准差

# print(np.cumsum(a))  # 累加 [ 0  1  3  6 10 15 21 28]

# 利用布尔值判断阵列中的内容
# a = np.array([35, 65, 33, 53, 76, 12, 33])
# print(a < 50)  # [ True False  True False False  True  True]

# numpy阵列运算
# A = np.array([[1, 1], [3, 3]])
# B = np.array([[2, 2], [5, 5]])

# print(A*B)
# print(A.dot(B))
# print(np.dot(A, B))
# print(np.sqrt(B))
# print(np.exp(A))

# 向量阵列的内/外积运算
a = np.array([1, 4, 7], float)
b = np.array([2, 5, 8], float)
print(np.inner(a, b))
print(np.cross(a, b))

# a = np.array([[1, 2], [3, 4]])
# 转置矩阵
# print(a.T)

# 反矩阵
# a_rev = np.linalg.inv(a)
# print(a_rev)

# 垂直方向合并
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 0], [0, 0]])
# V = np.vstack((A, B))
# H = np.hstack([A, B])
# print(V, H, end="\n\r", sep='\n')
