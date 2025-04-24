# 1 Counter统计元素频率
from collections import Counter

# 假设我们有一个点云标签数据
labels = ["car", "pedestrian", "car", "tree", "car", "tree", "pedestrian"]

# 使用 Counter 统计各类标签的频次
label_count = Counter(labels)

print(label_count)

# 2 defaultdict自动处理缺失键
from collections import defaultdict

# 默认值设为list类型
data = defaultdict(list)

data["car"].append([1,2,3])
data["pedestrian"].append([4,5,6])

print(data)

# 3 deque 双端列表
# 相比列表，deque 在两端操作的时间复杂度是 O(1)，而在列表的两端操作是 O(n)。
from collections import deque
# 创建一个空的双端列表
queue = deque()

# 队列右侧添加元素
queue.append(1)
queue.append(2)

# 从队列左侧添加元素
queue.appendleft(0)

# 删除并返回队列最右侧元素
queue.pop()
print(queue)

# 删除并返回队列左侧元素
queue.popleft()
print(queue)

# 4 namedtuple 命名元组
# namedtuple 允许创建一个具备命名字段的元组，使得元组元素能通过字段名来访问，而不是仅通过索引。它代码更具可读性。
from collections import namedtuple

# 定义一个点云数据元组
Point = namedtuple("Point",["x","y","z"])

# 创建一个点
point = Point(1,2,3)
print(point.x,point.y,point.z)


