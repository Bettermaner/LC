# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"

# 方法	时间复杂度	空间复杂度
# 解法一：动态规划	O(n)	O(n)
# 解法二：栈	O(n)	O(n)
# 解法三：双向遍历	O(n)	O(1)

# 解法一：动态规划
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



# 🧠 解法二：使用 栈（Stack）
# 💡 思路
# 使用栈来记录左括号的位置索引。并用一个变量 start 来记录无效右括号的位置或上一个不匹配的位置。

# 遇到 '('，将它的下标压入栈
# 遇到 ')'：
# 如果栈为空，说明当前没有可以匹配的 '('，更新 start
# 如果栈不为空，弹出一个元素，并计算当前有效长度

def longestValidParentheses(s: str) -> int:
    stack = [-1]  # 初始放入 -1，用于处理边界情况
    max_len = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len


# 🧠 解法三：两次遍历（从左到右 + 从右到左）
# 💡 思路
# 第一次从左往右扫描，统计左右括号数量，当 left == right 时更新最大值
# 第二次从右往左扫描，同样逻辑，防止漏掉某些情况

def longestValidParentheses(s: str) -> int:
    left = right = max_len = 0

    # 从左到右扫描
    for char in s:
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_len = max(max_len, right * 2)
        elif right > left:
            left = right = 0

    left = right = 0

    # 从右到左扫描
    for char in reversed(s):
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_len = max(max_len, left * 2)
        elif left > right:
            left = right = 0

    return max_len


