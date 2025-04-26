# 解题思路
    # 动态规划
    # 状态转移方程:dp[i][j] = (dp[i-1][j] + dp[i][j-1])
    # 初始值 : dp[0][0] = 1
    # 边界值: dp[i][0] = 1, dp[0][j] = 1


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        #print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    

from typing import List

def uniquePaths(m: int, n: int) -> int:
    # 创建dp表，m行n列
    dp = [[0] * n for _ in range(m)]
    
    # 初始化起点
    dp[0][0] = 1
    
    # 初始化第一列
    for i in range(1, m):
        dp[i][0] = dp[i-1][0]
    
    # 初始化第一行
    for j in range(1, n):
        dp[0][j] = dp[0][j-1]
    
    # 填充dp表
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # 返回右下角的值，即为不同路径总数
    return dp[m-1][n-1]

# 示例
m = 3
n = 7
print(uniquePaths(m, n))  # 输出应该是28