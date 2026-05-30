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
