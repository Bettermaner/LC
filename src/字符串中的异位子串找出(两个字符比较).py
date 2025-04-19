# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

#输入: s = "cbaebabacd", p = "abc"
#输出: [0,6]
#解释:
#起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
#起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。


# 方法1，看起来好理解，容易实现，但是性能低
def run(s,p):
    if len(s) < len(p):
        return []
    
    sorted_p = sorted(p)

    p_len = len(p)

    res = []


    for  i in range(len(s)-p_len+1):
        cur_string = sorted(s[i:i+p_len])
        if cur_string == sorted_p:
            res.append(i)

    return res



# 方法2，滑动窗口+哈希表
# 哈希表1记录p字符中，每个字符的出现频率，哈希表2记录滑动窗口内的哈希表2，每个字符出现的频率，每次比较两个哈希表，是否相当，若相当则是异位子串，加入


def run(s,p):
    if len(s) < len(p):
        return []
    
    w_count = {}
    p_count = {}

    p_len = len(p)

    res = []

    for i in range(p_len):
        p_count[p[i]] = p_count.get(p[i],0) + 1

    for i in range(p_len):
        w_count[s[i]] = w_count.get(s[i],0) + 1

    if w_count == p_count:
        res.append(0)

    for i in range(p_len,len(s)):
        # 滑动时，移除窗口左边的字符
        if w_count[s[i-p_len]] == 1:
            del w_count[s[i-p_len]]
        else:
            w_count[s[i-p_len]] -= 1
        # 滑动时，添加右边窗口的字符
        w_count[s[i]] =  w_count.get(s[i],0) + 1
    
        if w_count == p_count:
            res.append(i-p_len + 1)

    return res

s = "cbaebabacd"
p = "abc"
    
print(run(s,p))