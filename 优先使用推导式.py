import dis
# 将 Python 源码编译后的字节码指令打印出来，字节码是 Python 运行的底层语言（交给解释器执行的）

# 普通循环创建列表
def normal_loop():
    res = []
    for i in range(1000):
        res.append(i*2) #  0 到 999，每次都乘以 2
    return res

# 列表推导式
def list_comp():
    return [i*2 for i in range(1000)] # 写法更精简，性能更高

# 查看字节码差异
print("普通循环字节码:")
dis.dis(normal_loop)

print("\n推导式字节码:")
dis.dis(list_comp)
"""
普通循环用了 .append()、CALL、POP_TOP 等通用指令（慢）
推导式用了 LIST_APPEND 这种 专门优化的指令（快）
"""


# 性能对比
import timeit

t_loop = timeit.timeit('normal_loop()', globals=globals(), number=100000)
t_comp = timeit.timeit('list_comp()', globals=globals(), number=100000)
"""
timeit.timeit() 会运行指定代码 number 次（这里是 10 万次），返回总耗时。
globals=globals() 是为了让 timeit 能访问之前定义的函数。
"""

print(f"普通循环时间: {t_loop:.5f}s")
print(f"列表推导式时间: {t_comp:.5f}s")  # 通常快20%-30%

# 普通循环时间: 3.38680s
# 列表推导式时间: 2.50909s
# 推导式比普通循环 快了大概 26%