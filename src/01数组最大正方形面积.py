# 解题思路
    # 动态规划

# dp[i][j]表示当以这个点为右下角时,最大正方形的边长值
# 找出最大边长即平方就可求出最大面积

# 当max[i][j] == 0,说明当前位置为0，所以不可能构成正方形，dp[i][j] = 0
# 当max[i][j] == 1,需要看该节点左边、上边、左上边的节点dp值，取三者的最小值 并加 1。
# 当max[i][j]在 上边缘，或者左边缘时，最大正方形边长只能为1

# 状态转移方程
# max[i][j] == 0 , dp[i][j] = 0
# max[i][j] == 1, dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1

# i = 0 or j = 0, dp[i][j] = 1

def func(maxt):

    m = len(maxt)
    n = len(maxt[0])

    dp = [[0 for i in range(n)] for i in range(m)]
    
    max_side = 0

    for i in range(m):
        for j in range(n):

            if (i ==0 or j == 0):
                dp[i][j] = 1

            else:
                if maxt[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1]) + 1

            max_side = max(max_side,dp[i][j])

    return max_side ** 2

            


