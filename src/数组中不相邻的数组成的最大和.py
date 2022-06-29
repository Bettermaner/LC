# 解题思路
    # 动态规划
    # i表示当前总共几个数的情况下
    # dp[i] = max(dp[i-2] + array[i], dp[i-1] )
    # dp[0] = array[0]