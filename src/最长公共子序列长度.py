# 解题思路
    # 动态规划
    # i表示string1的i个字,j表示string2的j个字符
    # dp[i][j] 表示在string1 i个字符与string2 j个字符的情况下，最长公共子序列长度
    # 初始值 dp[0][j] = 0, dp[i][0] = 0
    # 状态转移方程 if string1[(i-1)] = string2[(j-1)], dp[i][j] = dp[i-1][j-1] + 1
    # if string1[(i-1)] != string2[(j-1)], dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    # 这里和最长重复子数组的区别在于，前者是不需要连续相邻，后者需要连续相邻

def func(string1,string2):

    n = len(string1)
    m = len(string2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1,n+1):

        for j in range(1,m+1):
            
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    return dp[n][m]