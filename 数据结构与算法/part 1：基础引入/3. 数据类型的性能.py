# 比较四种生成列表方式的性能差异（以生成前1000个整数的列表为例）
# 1. 循环连接列表
def func1():
    list1 = []
    for i in range(1000):
        list1 += [i]

# 2. append方法
def func2():
    list2 = []
    for i in range(1000):
        list2.append(i)

# 3. 列表推导式
def func3():
    list3 = [i for i in range(1000)]

# 4. range转列表
def func4():
    list4 = list(range(1000))