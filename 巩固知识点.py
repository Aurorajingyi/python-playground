# 💕1、enumerate() 会把一个 可迭代对象（比如列表）变成一个 (索引, 元素) 形式的可迭代对象。

# 例1：遍历列表时取索引和值
fruits = ['apple','banana','cherry']
for index, fruit in enumerate(fruits):
    print(index,fruit)
"""
0 apple
1 banana
2 cherry
"""

# 例2：改变起始的索引号
for index, fruit in enumerate(fruits,start=1):print(fruit)
"""
1 apple
2 banana
3 cherry
"""

# 例3：构建带序号的字符串列表
labeled = [f"{idx+1}:{fruit}"for idx,fruit in enumerate(fruits)]
print(labeled)

# 💕2、zip()
# 💕zip.():可以把多个可迭代对象“一一配对”，生成一个“元组对”的可迭代对象。
# 1、将两个列表配对
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
for name, score in zip(names,scores):
    print(name,score)
    print(f"{name}got{score}")


# 2、转换成列表或字典
labeled = list(zip(names,scores))
print(labeled)
print(zip(names,scores)) # <zip object at 0x00000202F0A7B680>
pairs = dict(zip(names,scores))
print(pairs)

# 3、解压
pairs = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
# 解压回两个列表（加星号 * 解包）
Names, Scores = zip(*pairs)
print(Names)
print(Scores)

# 4、配合enumerate使用
for i,(name,score) in enumerate(pairs):
    print(f"{i+1}:{name},{score}")

# 💕列表推导式
# 旧方法写平方
squires = []
for i in range(5):
    squires.append(i*i)
# 新写法
squires = [i*i for i in range(5)]
print(squires)
# 加条件
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# 套函数
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)

# 💕字典推导式
d = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# !!从列表转dict
pairs = [('a',1),('b',2)]
# 列表里放了两个元组，('a',1)第一个元组，长度为2
dic = {key: value for key, value in pairs}
print(dic)

# 💕 二维数组:python没有真正的数组，只有数组的嵌套
matrix = [
    [1,2,3],
    [4,5,6]
]
# 访问元素
print(matrix[0][1]) # 访问第0行第1列（2）

# 遍历二维数组
for row in matrix:
    for item in row:
        print(item,end=" ") # 不换行，空格
print()
#💕二维数组高频考点
zero = [[0 for _ in range(4)] for _ in range(3)]
print(zero)