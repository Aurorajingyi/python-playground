"""
- 如有变量 goods = ['汽车','飞机','火箭'] 提示用户可供选择的商品：

  ```python
  0,汽车
  1,飞机
  2,火箭
  ```

- 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。
"""
goods = ['汽车','飞机','火箭']
for index,good in enumerate(goods):
    print(f"{index},{good}")
num = int(input("请输入索引："))
try:
    if 0<=num<len(goods):
        print(goods[num])
    else:
        print("你输入的数字不在有效范围")
except ValueError:
    print("请输入数字！")