# 变位词：构成字母相同，但位置不同的英文单词，如heart和earth
# 判断两个单词是否是变位词

# 尝试
# 思路：将两个单词转换为集合，因为集合有无序性，所以无需考虑字母顺序，只需考虑集合内元素是否相等即可，有重复字母同样成立
# 时间复杂度为O(n)，n为单词字符串长度
def check(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    if set1 == set2:
        return True
    else:
        return False

result_a = check("heart", "earth")
print(result_a)
result_b = check("apple", "ppale")
print(result_b)

# 视频解法1：逐字检查，将一个单词的字符逐个到第二个单词中检查，存在就做标记，避免后面的重复检查
# 时间复杂度为O(n^2)
# 打勾标记：设置成None即可
def check1(s1, s2):
    l2 = list(s2) # 因为字符串是不可变类型，所以先将其转换为列表类型，便于后面的标记
    index1 = 0 # 用以遍历s1
    result = True # 该结果为最后的判断结果
    while index1 < len(s1) and result:
        index2 = 0 # 用以遍历l2
        found = False # 循环标记，标记是否找到相同字符
        while index2 < len(s2) and not found:
            if s1[index1] == l2[index2]:
                found = True
            # 如果有相同的字符，就是找到了，found就赋值为True
            else:
                index2 += 1 # 如果没找到，继续向下一个字符寻找
        if found:
            l2[index2] = None # 找到了，打勾标记
        else:
            result = False
            # 没找到，就不是变位词，result赋值为False
            # 由于不符合外层循环条件，自动跳出外层循环
        index1 += 1 # 继续遍历s1，判断下一个字符
    return result

result1 = check1("apple", "ppale")
print(result1)

# 视频解法2：排序比较，先将两个字符串按照字母顺序排序，再比较排序后的字符串是否相同
# 时间复杂度为O(n * log n)，主导的步骤是排序步骤
# 视频中的讲解是，排好序后再逐字比较，个人认为稍微有点麻烦了，因为字符串可以直接比较，但是也是一个很好的方法
# index = 0 # 该下标用于同时遍历两个下标
# result = True # 对比结果，控制循环的条件
# while index <= len(ss1) and result:
#     if ss1[index] == ss2[index]: # 直接同时遍历并比较
#         index += 1 # 相同则比较下一位
#     else:
#         result = False # 不相同，则不是变位词，结果改为False
# return result
def check2(s1, s2):
    ss1 = sorted(s1)
    ss2 = sorted(s2)
    # 将两个字符串按照字母表顺序进行排序
    if ss1 == ss2: # 比较排序后的字符串是否相同
        return True
    else:
        return False

result2 = check("python", "typhon")
print(result2)

# 视频解法3：暴力法，将第一个字符串的所有字母做全排列，判断第二个字符串是否存在于全排列中
# 暴力法，就是穷尽所有的可能组合
# 如果一个字符串包含n个字符，则所有可能的结果共有n!个，太多了，所以不推荐这个算法
# 可以使用标准库itertools.permutations来获取全排列，该函数返回一个元组
import itertools as it # 调用itertools库以使用permutations函数
def permutation(s):
    total = [''.join(i) for i in it.permutations(s)]
    # 1. it.permutations(s)：得到s字符串中字母的全排列，并返回一个元组
    # 2. for循环：遍历该元组
    # 3. ''.join(i)：将元组中的元素通过join()拼接成字符串，''表示拼接时元素之间没有其他字符
    # 4. 全排列的结果在全部转换为字符串之后，存储在total列表中
    return total

def check3(s1, s2):
    total1 = permutation(s1) # 用第一个字符串的所有字母做全排列
    result = True # 比较结果
    for i in total1: # 遍历全排列
        if i == s2:
            break
        # 如果第二个字符串在全排列中，则两字符串相同，是变位词
    return result

result3 = check("pythom", "typhon")
print(result3)

# 视频解法4：计数比较，如果两个字符串的字母出现的次数一样，则两个字符串是变位词，只需统计两个字符串的字母的出现次数
# 个人想法：可用字典存储每个字母出现的次数，再比较字典是否相等
def check4(s1, s2):
    d1 = {}
    d2 = {}
    # 定义两个空字典来存储两个字符串的字母出现情况
    for i in s1:
        d1[i] = d1.get(i, 0) + 1
    for i in s2:
        d2[i] = d2.get(i, 0) + 1
    # 分别对两个字符串进行遍历，并修改字母出现情况
    # get()：如果键存在，返回键对应的值；如果键不存在，返回默认值
    if d1 == d2: # 直接比较两个字典，判断是否为变位词
        return True
    else:
        return False

result4 = check("python", "typhon")
print(result4)