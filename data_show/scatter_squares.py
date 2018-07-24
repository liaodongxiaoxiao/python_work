import matplotlib.pyplot as plt

# x_value = [1, 2, 3, 4, 5]
# y_value = [1, 4, 9, 16, 25]

x_value = list(range(1, 1001))
y_value = [x ** 2 for x in x_value]

# edgecolors='none' 不显示点的轮廓
# plt.scatter(x_value, y_value, edgecolors='none', s=40)
# c ='red' 点的颜色 或 c =(r,g,b) r g b 为 0~1
# plt.scatter(x_value, y_value, c=(0, 0, 0.8), edgecolors='none', s=40)

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)

plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

# plt.show()
# 自动保存 bbox_inches="tight" 裁掉空白区域
plt.savefig('squares_plot.png', bbox_inches="tight")
