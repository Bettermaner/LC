# 解题思路
    # 动态规划
    # dp[i][j]表示当前所处在数组的位置时，路径上的数和最小的路径
    # 状态转移方程: dp[i][j] = min(dp[i-1][j] + mat[i][j] ,dp[i][j-1]+ mat[i][j] )
    # 初始值: dp[0][0] = mat[0][0]
    # 边界值：dp[i][0] = dp[i-1][0] + mat[i][0], dp[0][j] = dp[0][j-1] + mat[0][j]

from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    
    # 创建dp表
    dp = [[0] * n for _ in range(m)]
    
    # 初始化起点
    dp[0][0] = grid[0][0]
    
    # 初始化第一行
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # 初始化第一列
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # 填充dp表
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # 返回右下角的值，即为最小路径和
    return dp[m-1][n-1]

# 示例
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(minPathSum(grid))  # 输出应该是7