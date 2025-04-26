# 解题思路
    # 将+的数据的和看成x,将-的数的和看出y

    # x + y = target， x - y = sum(array) -> -y = (sum(array) - target) / 2
    # (sum(array) - target) 需要被2整除 ,不然就不存在组合

    # 找出和为 (sum(array) - target) / 2的组合数即可
    # 动态规划,dp[i][j] i表示总共几个数的情况下，j表示总和为多少
    # 转移方程：array[i] > j, dp[i][j] = dp[i -1][j]
    #           array[i] =< j, dp[i-1][j-array[i]] + 1 
    # 初始状态: j = 0时，dp[0][j] = 1, j>0 时，dp[0][j] = 0


# 给你一个整数数组 nums 和一个整数 target 。

# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目

# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3


def func(array,target):

    sum = 0
    for v in array:
        sum += v
    
    if (sum - target) % 2 != 0 or sum - target < 0:
        return 0

    diff = int((sum - target ) / 2)

    dp = [0 for i in range(diff + 1)]
    dp[0] = 1

    for i in range(1,diff+1):
        for v in array:
            # 举例： 装满dp[5]
            # 若
            # 已经有一个为1的nums[i]，有dp[4]种方法
            # 已经有一个为2的nums[i]，有dp[3]种方法
            # 已经有一个为3........,...dp[2]种方法
            # ............5 .......,....dp[0]
            # 综上dp[5]=dp[4]+dp[3]+dp[2]+dp[1]+dp[0]
            # dp[j]=dp[j-nums[i]]

            if v <= i:
                dp[i] += dp[i-v]

    return dp[diff]


print(func([1,1,1,1,1],3))