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

# 使用timeit模块对四种方式进行计时，比较性能差异
from timeit import Timer
t1 = Timer("func1()", "from __main__ import func1")
print(t1.timeit(number=1000))
t2 = Timer("func2()", "from __main__ import func2")
print(t2.timeit(number=1000))
t3 = Timer("func3()", "from __main__ import func3")
print(t3.timeit(number=1000))
t4 = Timer("func4()", "from __main__ import func4")
print(t4.timeit(number=1000))
# 结果：func1 > func2 > func3 > func4

# 列表操作中的pop，如果是pop()，即删除列表的最后一个元素，时间复杂度是O(1)
# 如果是pop(i)，即删除列表中的第i个元素，时间复杂度是O(n)
# 因为如果是pop(i)，python会把第i个元素后的每一个元素向前挪位复制一遍
# 但是，这种向前挪位复制一遍的方法，又能使得按索引取值和赋值的时间复杂度是O(1)
# 这体现出了对于常用操作和不常用操作的折中思想

# list.pop的计时检验
pop_empty = Timer("x.pop()", "from __main__ import x")
pop_zero = Timer("x.pop(0)", "from __main__ import x")

print("pop(0)    pop()")
# 改变列表x的长度
for i in range(10000, 1000001, 50000):
    x = list(range(i))
    pz = pop_zero.timeit(number=1000)
    x = list(range(i))
    pe = pop_empty.timeit(number=1000)
    print(f"{pz: 5.5f}, {pe: 5.5f}")
# 通过改变列表长度，发现pop()的时间随列表长度改变而发生的变化很小
# 但pop(i)的时间变化比较明显
# 如果将两者的时间画成图表，可以发现pop()是常值函数，但pop(i)是线性增加的