import timeit
def dynamic_append():
    res = []
    for i in range(100000):
        res.append(i)
    return res

def preallocated():
    res = [None] * 100000
    for i in range(100000):
        res[i] = i
    return res

print("动态扩展耗时:", timeit.timeit(dynamic_append, number=1000))
print("预分配耗时:", timeit.timeit(preallocated, number=1000))

"""
动态扩展耗时: 2.5800792000009096
预分配耗时: 2.149861300000339
"""
