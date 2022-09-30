# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

#  

# 示例 1:

# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]


# 解题 思路
    # 排序加哈希


def func(array):
    m = {}

    for i in array:
        t = sorted(i)
        key = ",".join(t)
        if key not in m:
            m[key] = []
        m[key].append(i)

    return list(m.values())

print(func(["eat", "tea", "tan", "ate", "nat", "bat"]))