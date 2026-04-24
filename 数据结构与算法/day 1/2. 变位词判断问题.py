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

# result1 = check("heart", "earth")
# print(result1)
# result2 = check("apple", "ppale") # 仅为测试代码，测试有重复字母是否可行，没有ppale这个单词哈
# print(result2)

# 视频解法1：逐字检查，将一个单词的字符逐个到第二个单词中检查，存在就做标记，避免后面的重复检查
# 时间复杂度为O(n^2)
# 打勾标记：设置成None即可
def check2(s1, s2):
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

result1 = check2("apple", "ppale")
print(result1)





