# 给定一个整数矩阵，找出最长递增路径的长度。
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

# 解题思路
    # dfs + 动态规划

    # 首先需要一个dfs方法。以向左递归为例，如果matrix[i-1][j]<=matrix[i][j]则返回0；否则继续向四个方向递归。dfs方法需要判断边界。
    # 然后需要一个跟matrix一样大的二维数组int[][] dp，记录已经计算出来的每一个点的最长递增路径，防止重复计算。


import re


def func(matrix):

    res = 0
    m = len(matrix)
    n = len(matrix[0])

    dp = [[0 for j in range(n)]for i in range(m)]

    for i in range(m):
        for j in range(n):
            
            res = max(dfs(matrix,dp,i,j,0),res)
    
    return res


def dfs(matrix,dp,i ,j ,pre_val):

    # 边界条件以及是否递增
    if (i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or pre_val >= matrix[i][j]):
        return 0

    # 说明已经被统计过了，直接返回结果
    if dp[i][j] != 0:
        return dp[i][j]

    max_left = dfs(matrix,dp,i-1,j,matrix[i][j])
    max_right = dfs(matrix,dp,i+1,j,matrix[i][j])
    max_up = dfs(matrix,dp,i,j-1,matrix[i][j])
    max_down = dfs(matrix,dp,i,j+1,matrix[i][j])

    dp[i][j] = max(max(max_left,max_right),max(max_up,max_down)) + 1

    return dp[i][j]
            
         