# 解题思路
    # 动态规划
    # i表示string1的i个字,j表示string2的j个字符
    # dp[i][j] 表示在string1 i个字符与string2 j个字符的情况下，最长公共子序列长度
    # 初始值 dp[0][j] = 0, dp[i][0] = 0
    # 状态转移方程 if string1[(i-1)] = string2[(j-1)], dp[i][j] = dp[i-1][j-1] + 1
    # 这里和最长公共子序列的区别在于，前者是需要连续相邻的子数组，后者需要不需要连续

def func(array1,array2):
    n = len(array1)
    m = len(array2)

    dp = [0 for i in range(n+1) for j in range(m+1) ]

    max_length = 0

    for i in range(1,n+1):

        for  j in range(m+1):

            if array1[i-1] == array2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
            max_length = max(dp[i][j],max_length)

    return max_length

