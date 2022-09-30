# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
# 如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"

# 解题思路
    # 滑动窗口
    # 如何判断滑动窗口包含了T的所有元素？

    # 我们用一个字典need来表示当前滑动窗口中需要的各元素的数量，
    # 一开始滑动窗口为空，用T中各元素来初始化这个need，当滑动窗口扩展或者收缩的时候，去维护这个need字典，
    # 例如当滑动窗口包含某个元素，我们就让need中这个元素的数量减1，代表所需元素减少了1个；
    # 当滑动窗口移除某个元素，就让need中这个元素的数量加1。

    # 记住一点：need始终记录着当前滑动窗口下，我们还需要的元素数量，我们在改变i,j时，需同步维护need。
    # 值得注意的是，只要某个元素包含在滑动窗口中，我们就会在need中存储这个元素的数量，如果某个元素存储的是负数代表这个元素是多余的。
    # 比如当need等于{'A':-2,'C':1}时，表示当前滑动窗口中，我们有2个A是多余的，同时还需要1个C。
    # 这么做的目的就是为了步骤二中，排除不必要的元素，数量为负的就是不必要的元素，而数量为0表示刚刚好。
    # 回到问题中来，那么如何判断滑动窗口包含了T的所有元素？结论就是当need中所有元素的数量都小于等于0时，表示当前滑动窗口不再需要任何元素。

    # 优化
    # 如果每次判断滑动窗口是否包含了T的所有元素，都去遍历need看是否所有元素数量都小于等于0，这个会耗费O(k)O(k)的时间复杂度，k代表字典长度，最坏情况下，k可能等于len(S)。
    # 其实这个是可以避免的，我们可以维护一个额外的变量needCnt来记录所需元素的总数量，
    # 当我们碰到一个所需元素c，不仅need[c]的数量减少1，同时needCnt也要减少1，
    # 这样我们通过needCnt就可以知道是否满足条件，而无需遍历字典了。
    # 前面也提到过，need记录了遍历到的所有元素，而只有need[c]>0大于0时，代表c就是所需元素

def func(s,t):

    need = {}
    for i in t:
        if i not  in need:
            need[i] = 0
        need[i] += 1

    need_cnt = len(t)

    res = [0,len(t)+1]

    left = 0

    for right ,value in enumerate(s):
        if value not in need:
            need[value] = 0
        if need[value] > 0:
            need_cnt -= 1
        need[value] -= 1

        if need_cnt == 0: #步骤一：滑动窗口包含了所有T元素
            while True: #步骤二：增加i，排除多余元素
                left_value = s[left]
                if need[left_value] == 0:
                    break
                need[left_value] += 1
                left += 1

            if right - left < res[1] - res[0]:  #记录结果
                res = [left,right]

            need[left_value] += 1 #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
            need_cnt += 1
            left += 1

    return "" if res[1] > len(s) else s[res[0]:res[1]+ 1] #如果res始终没被更新过，代表无满足条件的结果

print(func("ADOBECODEBANC","ABC"))