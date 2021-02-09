# coding=utf-8
from matplotlib import pyplot as plt


x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 设置图片大小
fig = plt.figure(figsize=(18, 8), dpi=80)

# 绘图
plt.plot(x, y)

# 设置x轴的刻度
# plt.xticks(x)

# _xtick_lables = [i/2 for i in range(4, 49)]
# plt.xticks(_xtick_lables)

# plt.xticks(range(2, 25))
# plt.xticks(_xtick_lables[::3])

# plt.yticks(range(min(y), max(y)+1))

# 展示图形
plt.show()

# 保存图片（可以保存为。svg的格式放到网页上）
# # plt.savefig("./fig_size.png")
