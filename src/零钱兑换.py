# 解题思路
    # 动态规划
    # 假设i表示需要兑换的金额， 有j种零钱，每种零钱个数无上限
    # 转移方程：dp[i] = min(dp[i - coin[0]] + 1,dp[i -coin[1] + 1, .....,dp[i-coin[j] + 1]]
    # 初始值： dp[0] = 0