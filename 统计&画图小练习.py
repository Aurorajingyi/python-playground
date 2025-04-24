import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 模拟类别标签
categories = ['car', 'pedestrian', 'cyclist']

# 随机生成 100 条检测结果
np.random.seed(42)  # 用来固定随机数，保证可复现
data = {
    'class': np.random.choice(categories, size=100, p=[0.5, 0.3, 0.2]),  # 类别
    'score': np.random.uniform(0.5, 1.0, size=100)  # 从 0.5 到 1.0 的范围内生成随机浮点数（连续分布）
}

# 构建 DataFrame，类似于excel表
df = pd.DataFrame(data)

# 按类别统计数量
class_counts = df['class'].value_counts()

# 可视化
plt.figure(figsize=(8, 4))
plt.bar(class_counts.index, class_counts.values, color='skyblue')
plt.title("Category Detection Statistics (Simulated Data)")
plt.xlabel("Category")
plt.ylabel("Quantity")
plt.tight_layout() # 自动调整子图间距
plt.show()
