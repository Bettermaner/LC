# 解题思路
    # 动态规划
    # dp[i] 表示以i索引对应的数作为子序列结尾时对应的最长长度
    # 初始值 dp[i] = 1,因为子递增序列至少长度为1
    # 转移方程 if num[i] > num[j] ,dp[i] = dp[j] + 1,   j 表示比i小的索引，依次遍历得到

def func(array):

    n = len(array)

    dp = [1 for i in range(n)]

    result = 1 

    for i in range(n):

        j = 0
        while j <= i:
            if array[i] > array[j]:
                dp[i] = max(dp[i],dp[j] + 1)

        result = max(result,dp[i])

    return result