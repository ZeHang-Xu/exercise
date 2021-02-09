# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=fr"C:\Windows\Fonts\simkai.ttf", size=12)

y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
x = range(11, 31)

plt.figure(figsize=(16, 8), dpi=80)

plt.plot(x, y1, label='自己', color='cyan', linestyle='-.', linewidth=1, alpha=0.5)
plt.plot(x, y2, label='同桌', color='pink', linestyle=':')

# 设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels, fontproperties=my_font)
plt.yticks(range(10))

# 添加网格
plt.grid(alpha=0.4)

# 添加图列
plt.legend(prop=my_font, loc='best')  # loc: [0, 1,2, ..., 8]

plt.show()
