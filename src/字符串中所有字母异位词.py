# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

# 解题思路
    # 滑动窗口

def func(s,p):
    s_l , p_l = len(s),len(p)

    if s_l < p_l:
        return []
    res = []
    s_count = [0] * 26
    p_count = [0] * 26

    for i in range(p_l):
        s_count[ord(s[i]) - 97] += 1
        p_count[ord(p[i]) - 97] += 1

    if s_count == p_count:
        res.append(0)

    for i in range(s_l-p_l):
        s_count[ord(s[i]) - 97 ] -= 1 
        s_count[ord(s[i + p_l ]) - 97] += 1 

        if s_count == p_count:
            res.append(i+1)

    return res

print(func("cbaebabacd","abc"))