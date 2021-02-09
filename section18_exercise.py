# 如果列表a表示10点到12点的每一分钟的气温，如何绘制折线图观察每分钟的气温变化情况？
# a = [random.randint(20, 35) for i in range(120)]
import random
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager


# # Windows和Linux设置字体的方式
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 10}
# matplotlib.rc('font', **font)


# 另外一种设置字体大小的方式
my_font = font_manager.FontProperties(fname=fr"C:\Windows\Fonts\方正粗黑宋简体.ttf")


x = range(120)
y = [random.randint(20, 35) for i in range(120)]

# 设置图片大小
plt.figure(figsize=(18, 8), dpi=80)

# 绘图
plt.plot(x, y)

# 调整x轴刻度
_x = list(x)
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
# 保证iterator和labels一一对应,步长一致
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45)  # rotation旋转的度数
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45, font_properties=my_font)  # rotation旋转的度数


# 添加坐标轴的描述信息
plt.xlabel('时间 (min)', fontproperties=my_font)
plt.ylabel('温度 (℃)', fontproperties=my_font)
plt.title('10点到12点每分钟的气温变化情况', fontproperties=my_font)

# 添加网格
plt.grid(alpha=0.4)

# 展示图形
plt.show()
