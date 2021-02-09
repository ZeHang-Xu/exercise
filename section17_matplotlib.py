# %matplotlib inline
import matplotlib  # 注意这个也要import一次
import matplotlib.pyplot as plt

# plt.legend(loc='best',
#            framealpha=0.5,
#            prop={'size': 'small', 'family': 'monospace'})  # prop属性(字体大小，字体类型)
# plt.show()
#
# plt.title('random trends')
# plt.xlabel('Date')
# plt.ylabel('Cum.sum')
# # 使用figtext方法可以添加文字
# plt.figtext(0.995, 0.01, u'\u00a9 acme designed 2018', ha='right', va='bottom')  # 水平对齐，va垂直对齐
# plt.show()

# plt.subplot(321)
# plt.subplot(322)
# plt.subplot(323)
# plt.subplot(324)
# plt.subplot(325)
# plt.subplot(326)
# plt.show()


import numpy as np

t = np.arange(0.01, 5, 0.01)
# print(t)
s1 = np.sin(2*np.pi*t)
s2 = np.exp(-t)
s3 = np.sin(4*np.pi*t)

ax1 = plt.subplot(311)
plt.plot(t, s1)

plt.show()
