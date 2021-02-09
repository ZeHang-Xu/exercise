# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=fr"C:\Windows\Fonts\simkai.ttf", size=12)

# 统计后的数据不能绘制直方图
interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 57]

# print(len(interval), len(width), len(quantity))

plt.bar(range(len(quantity)), quantity, width=1)

# 设置x轴的刻度
_x = [i-0.5 for i in range(13)]
_xticks_labels = interval + [150]
plt.xticks(_x, _xticks_labels)

plt.grid(alpha=0.4)

plt.show()
