# 共变异数 covariance（协方差）                         Cov(X, Y)
# 共变异数量测两个变数同时变化的情况                      =E(XY) - E(X)E(Y)
# 单一变数的协方差 -> 变异数 （variance）               =E(XY) - |XY|
# Cov(x,y)之正负 -> 反应 x, y资料变化的方向相同或相反


# covariance 共变异数 --》衡量两个变数的误差
# 如果两个变数是统计独立的话则共变异数为0
import numpy as np
import pandas as pd

# s1 = pd.Series(np.random.randn(10))
# s2 = pd.Series(np.random.randn(10))
# print(s1.cov(s2))

frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
# print('元素a对b的共变异数: {}'.format(frame['a'].cov(frame['b'])))
print('共变异数矩阵:\n {}'.format(frame.cov()))


# 相关系数：值介于 -1 到 1 之间(完全负相关 ~ 完全正相关)             x和y的共变异数
# 应用在两变数间关联性的高低程度                            p=  ————————————————————
#                                                           x的标准差 * y的标准差

# print('元素a和b的相关系数: {}'.format(frame['a'].corr(frame['b'])))
print('相关系数矩阵:\n{}'.format(frame.corr()))
