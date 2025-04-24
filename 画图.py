# 1、折线图、柱状图、直方图
import matplotlib.pyplot as plt

# 折线图
x = [1,2,3,4]
y = [1,20,30,40]
plt.plot(x,y)
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title("Training Curve")
plt.show()

# 柱状图
categories = ['Car', 'Pedestrian', 'Cyclist']
counts = [123, 57, 30]
plt.bar(categories, counts)
plt.title("Detection Count per Class")
plt.show()

# 直方图
import numpy as np
scores = np.random.rand(1000) #随机生成1000个数
plt.hist(scores, bins=20) # 将1000个数据切分成20个区间块（条形柱），统计每个区间的数量。
print("Avg:", np.mean(scores))          # 预期 ~0.5
print("Std:", np.std(scores))        # 预期 ~0.29 (均匀分布标准差公式: sqrt(1/12))
print("Max:", np.max(scores))        # 接近1.0
print("Min:", np.min(scores))        # 接近0.0
plt.title("Score Distribution")
plt.show()

# 2、多子图
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
"""
生成一个 Figure 对象（画布）和一组 Axes 对象（子图坐标区）。
参数 1, 2：表示布局为1行 × 2列的形式，即横向并排两个子图。
figsize=(10,4)：设置画布的总大小为宽10英寸、高4英寸。
"""
axs[0].plot([1, 2, 3], [1, 4, 9])
axs[0].set_title("plot")

axs[1].bar(['A', 'B'], [5, 8])
axs[1].set_title("bar")

plt.tight_layout()
plt.show()

# 3、可视化点云视图
points = np.random.rand(1000, 2)
plt.scatter(points[:, 0], points[:, 1], s=1) # 生成点的大小为1像素
plt.title("2D point cloud Projection")
plt.axis("equal")
plt.show()


