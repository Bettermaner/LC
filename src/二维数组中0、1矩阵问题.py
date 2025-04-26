# 解题思路
    # 因为可以上下左右寻找最近0的距离，所以考虑双向动态规划
    # 一个动态规划只能考虑到上侧或者左侧的最近0的距离（下侧和右侧的数据还没有遍历到）
    # 考虑从左上角到右下角动态规划，再右下角到左上角动态规划。
    # 当 mat[i][j] = 0 ,dp[i][j] = 0
    # 1.dp[i][j] = min(dp[i-1][j] + 1,dp[i][j-1] + 1) , i > 0, j > 0
    # 2.dp[i][j] = min(dp[i+1][j] + 1, dp[i][j+1] + 1), i < len(mat) -1, j < len(mat[0]) -1

# 从左上到右下扫描：更新每个位置到其左边和上边的最近0的距离。
# 从右下到左上扫描：更新每个位置到其右边和下边的最近0的距离。

from typing import List

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    if not mat or not mat[0]:
        return []
    
    m, n = len(mat), len(mat[0])
    dist = [[float('inf')] * n for _ in range(m)]
    
    # 第一次扫描：从左上角到右下角
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
            else:
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
    
    # 第二次扫描：从右下角到左上角
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i < m - 1:
                dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
            if j < n - 1:
                dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
    
    return dist