# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"

# 解题思路
     # 动态规划

    # 首先，我们定义一个 dp 数组，其中第 ii 个元素表示以下标为 ii 的字符结尾的最长连续有效子字符串的长度。
    # 状态转移方程
    # if s[i] = "(",则dp[i] = 0,因为不可能有以"("结尾的括号
    # if s[i] = ")" and s[i-1] = "(", 则dp[i] = dp[i-2] + 2 
    
    # if s[i] = ")" and s[i-1] = ")"  and s[i-1 - dp[i-1]] = "("
    # 因为一旦s[i]和左边的“（”配对后，就成了一个单独的括号，可能与左边的字符组成连续括号,所以需要 + dp[i-1- dp[i-1] - 1]
    # 则 dp[i] = dp[i-1] + 2 + dp[i-1- dp[i-1] - 1]


def func(s):
    n = len(s)
    res = 0
    dp = [0 for i in range(n)]
    for i in range(1,n):
        if s[i] == "(":
            dp[i] = 0
        elif s[i] == ")":
            if s[i-1] == '(':
                dp[i] = dp[i -2] + 2
            elif s[i-1] == ")" and i-1 - dp[i-1] >= 0 and s[i-1 -dp[i-1]] == "(":
                dp[i] = dp[i -1] + 2 + dp[i-1-dp[i-1] -1 ]
        res = max(res,dp[i])

    return res

print(func("()(()())"))