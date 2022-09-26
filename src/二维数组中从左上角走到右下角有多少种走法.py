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