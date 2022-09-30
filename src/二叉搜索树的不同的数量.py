# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

# 输入：n = 3
# 输出：5

# 解题思路
    # 动态规划
    
    # dp[i] 表示在i个数的条件下，二叉搜索树的数量
    # dp[0] = 1, dp[1] = 1
    # 每当 根节点(j)不同，都会有 dp[j-1](左子树) + dp[i - j](右子树)种表示方式

def func(n):

    dp  = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        for j in range(i+1):
            dp[i] += dp[i-j] * dp[j-1]

    return dp[n]

print(func(3))