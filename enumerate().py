# enumerate 会把一个可迭代对象（比如列表）变成一个（索引，元素）形式的可迭代对象

# 1
fruits = ["apple","banana","cherry"]
for index, fruit in enumerate(fruits):
    print(index,fruit)

# 2
for index, fruit in enumerate(fruits,start = 1):
    print(index,fruit)

# 3 构建一个列表
labeled = [f"{index+1}:{fruit}" for index, fruit in enumerate(fruits)]
print(labeled)