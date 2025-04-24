# 将多个可迭代对象一一配对，生成一个个元组对
# 1
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78, 99] # 99用不到
for name, score in zip(names, scores):
    print(f"{name}:{score}")
# 2
scores_list=list(zip(names, scores))
scores_dict=dict(zip(names, scores))
print(scores_list)
print(scores_dict)
"""
[('Alice', 85), ('Bob', 92), ('Charlie', 78)]
{'Alice': 85, 'Bob': 92, 'Charlie': 78}
"""

# 3 解压
name,score = zip(*scores_list)
print(name)
print(score)

# 4
for i,(name,score) in enumerate(zip(names,scores),start=1):
    print(f"{i}:{name},{score}")

