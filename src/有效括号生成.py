# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]


# 解题思路:
    # 动态规划
    # 思路：
    # 当我们清楚所有 i<n 时括号的可能生成排列后，对与 i=n 的情况，我们考虑整个括号排列中最左边的括号。
    # 它一定是一个左括号，那么它可以和它对应的右括号组成一组完整的括号 "( )"，我们认为这一组是相比 n-1 增加进来的括号。

    # 那么，剩下 n-1 组括号有可能在哪呢？

    # 【这里是重点，请着重理解】

    # 这里的理解是关键 ！！！！！： 剩下的括号要么在这一组新增的括号内部，要么在这一组新增括号的外部（右侧）。 所以就有了 "(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】

    # 既然知道了 i<n 的情况，那我们就可以对所有情况进行遍历：

    # "(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】

    # 其中 p + q = n-1，且 p q 均为非负整数。

    # 事实上，当上述 p 从 0 取到 n-1，q 从 n-1 取到 0 后，所有情况就遍历完了。

    # 注：上述遍历是没有重复情况出现的，即当 (p1,q1)≠(p2,q2) 时，按上述方式取的括号组合一定不同。


# 综合以上分析，总体的时间复杂度可以估计为：
# 外层循环 O(n)
# 内层循环对于每个 i 需要处理 O(i * C_p * C_q) 的操作
# 总体来说，由于每个 dp[i] 的大小是卡特兰数级别的，所以总的时间复杂度大致为 O(n * 4^n / sqrt(n))

def func(n):
    if n == 0:
        return []
    dp = []

    dp.append([None]) # 当n= 0时的组合
    dp.append(['()']) # 当n=1时的组合

    for i in range(2,n+1):
        tmp = []
        for j in range(i):
            p = j
            q = i - 1 - p
            p_list = dp[p]
            q_list = dp[q]

            for p in p_list:
                for q in q_list:
                    if not p:
                        p = ""
                    if not q:
                        q = ""
                    l = "(" + p + ")" + q
                    tmp.append(l)
        dp.append(tmp)

    return dp[n]


print(func(3))


# 解放二：回溯法
# 我们可以使用递归的方式构造字符串：

# 当前字符串中 '(' 的数量为 left，')' 的数量为 right
# 只要满足 left <= n 和 right <= left，就可以选择添加新的括号：
# 如果 left < n，可以加 '('
# 如果 right < left，可以加 ')'
# 我们从空字符串开始，递归地构建所有可能的有效括号组合。


def generateParenthesis(n: int):
    result = []

    def backtrack(current: str, left: int, right: int):
        if len(current) == 2 * n:
            result.append(current)
            return
        # 如果还可以加左括号
        if left < n:
            backtrack(current + '(', left + 1, right)
        # 如果当前右括号比左括号少，可以加右括号
        if right < left:
            backtrack(current + ')', left, right + 1)

    backtrack("", 0, 0)
    return result