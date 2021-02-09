# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import font_manager


my_font = font_manager.FontProperties(fname=fr"C:\Windows\Fonts\simkai.ttf", size=12)

a = [169, 167, 160, 143, 122, 141, 166, 106, 144, 166, 147, 110, 175, 172, 165, 100, 168,
     130, 152, 109, 110, 152, 159, 122, 146, 132, 147, 143, 108, 147, 160, 101, 159, 112,
     166, 129, 167, 175, 139, 163, 155, 106, 168, 108, 147, 124, 148, 160, 107, 142, 117,
     121, 144, 126, 150, 108, 112, 156, 114, 123, 122, 160, 171, 105, 117, 123, 143, 123,
     131, 164, 147, 129, 148, 132, 170, 135, 152, 131, 161, 120, 117, 159, 149, 101, 141,
     109, 108, 151, 112, 163, 150, 174, 174, 102, 123, 121, 178, 116, 161, 174, 140, 142,
     168, 123, 166, 164, 134, 176, 105, 141, 156, 166, 149, 171, 156, 172, 133, 177, 172, 146]
# 计算组数
d = 3  # 组距

num_bins = (max(a) - min(a)) // d
print(num_bins)
plt.figure(figsize=(20, 8), dpi=80)

plt.hist(a, num_bins, density=1)  # density表示频率或密度

plt.xticks(range(min(a), max(a)+d, d))

plt.grid(alpha=0.4)

plt.show()
