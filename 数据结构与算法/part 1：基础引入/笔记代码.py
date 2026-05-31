# 调用time模块中的time函数，可以知道运行到该行代码时的时间
# 类型是浮点数，单位是秒，从1970.1.1的0时0分0秒开始计数
import time
a = time.time()
print(a)
print("hello")
time.sleep(10)
b = time.time()
print(b)
print(b - a)


# ord函数：可以将字符转换成在Unicode表中对应的数字，不仅限于英文
print(ord('a'))
print(ord('A'))
print(ord('你'))
print(ord(','))


# 使用timeit模块对函数进行计时，以测定函数的性能
# 核心：创建一个Timer对象，传入两个参数，一个是需要反复执行的语句，另一个是只需要执行一次的安装语句，都以字符串的形式传入
from timeit import Timer
def test1():
    c = 1
    d = 2
    e = c + d
def test2():
    f = 1 + 2

# 定义两个函数，并用timeit模块对两个函数进行计时
t1 = Timer("test1()", "from __main__ import test1")
print(t1.timeit(number=1000))
t2 = Timer("test2()", "from __main__ import test2")
print(t2.timeit(number=1000))
# number = 1000的意思是重复调用这个函数1000次，目的是通过多次重复运行，放大函数的运行时间，便于比较