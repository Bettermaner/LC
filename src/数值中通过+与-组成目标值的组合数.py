# 解题思路
    # 将+的数据的和看成x,将-的数的和看出y
    # x + y = target， x - y = sum(array) -> x = (sum(array) + target) / 2
    # (sum(array) + target) 需要被2整除 ,不然就不存在组合
    # 找出和为 (sum(array) + target) / 2的组合数即可
    # 动态规划,dp[i][j] i表示总共几个数的情况下，j表示总和为多少
    # 转移方程：array[i] > j, dp[i][j] = dp[i -1][j]
    #           array[i] =< j, dp[i-1][j-array[i]] + dp[i-1][j] 
    # 初始状态: j = 0时，dp[0][j] = 1, j>0 时，dp[0][j] = 0