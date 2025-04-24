"""
你在做一个行人检测系统，每一帧系统会输出所有检测到的行人 ID（假设系统能持续追踪并编号）：
要求：
统计每个行人 ID 出现的帧数（也就是在哪些帧被检测到了）。

找出出现次数最多的两个行人 ID。

输出这两个 ID 的列表，并按 ID 从小到大排序。

然后输出它们的总出现次数。

"""
from collections import Counter
from functools import reduce

frames = [
    [101, 102, 103],
    [101, 102],
    [101, 104],
    [101, 102, 104],
    [102, 104, 105],
]

# 1: 将所有帧的 ID 摊平
flat_ids =reduce(lambda x, y: x + y, frames)

# 2:统计次数
id_counter = Counter(flat_ids)
print(id_counter)
# Counter({101: 4, 102: 4, 104: 3, 103: 1, 105: 1})

# 3: 找出出现次数最多的两个id(先排序)
top2 = sorted(id_counter.items(), key=lambda x: (-x[1],x[0]))[:2]
# 按出现次数降序、ID升序；比如 [(101, 4), (102, 4)]
print(top2)

# 4:输出这两个 ID 的列表，并按 ID 从小到大排序
top2_ids = sorted(map(lambda x:x[0],top2))
print(top2_ids)

# 5:求他们出现的总次数
total = sum(map(lambda x:x[1],top2))
print("他们的总出现次数:",total)
