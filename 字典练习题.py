# 练习题
"""
结合下面的两个变量 header 和 stock_dict实现注意输出股票信息，格式如下：
	SH601778，股票名称:中国晶科、当前价:6.29、涨跌额:+1.92。
    SH688566，股票名称:吉贝尔、当前价:...               。
	...
"""
header = ['股票名称', '当前价', '涨跌额']

stock_dict = {
    'SH601778': ['中国晶科', '6.29', '+1.92'],
    'SH688566': ['吉贝尔', '52.66', '+6.96'],
    'SH688268': ['华特气体', '88.80', '+11.72'],
    'SH600734': ['实达集团', '2.60', '+0.24']
}
"""
方法一：
for keys, values in stock_dict.items():
    formatted=[]
    for index in range(len(header)):
        formatted.append(f"{header[index]}: {values[index]}")
    data = "、".join(formatted)
    print(f"{keys}: {data}")
"""


for keys, values in stock_dict.items():
    data = "、".join([f"{header[index]}: {values[index]}" for index in range(len(header))])
    print(f"{keys}: {data}")