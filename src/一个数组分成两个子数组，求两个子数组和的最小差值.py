# 解题思路
    # 动态规划
    # 求两个子数组的和的最小差值，实际就是让每个子数组的和尽量相等，则是求每个子数组的和的值尽量靠近 sum / 2
    # s1 + s2 = sum, s1 - s2 = diff, 则 diff = sum - 2(s2)
    # dp[i][j] : 表示有i个数的情况下，总的和最接近j的数的总和
    # 状态转移方程 
    # if array[i-1] < j, dp[i][j] = max(dp[i-1][j-array[i-1]] + array[i-1],dp[i-1][j]) else dp[i][j] = dp[i-1][j]
    # 初始值 dp[0][0] = 0 


def func(array):
    l = len(array)
    sum_value = sum(array)

    half_sum_value = sum_value / 2


    dp = [ [0 for j in range(int(half_sum_value)+1)] for i in range(l+ 1) ]

    for i in range(1,l+1):

        for j in range(1,int(half_sum_value) + 1):

            if array[i-1] <= j:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-array[i-1]] + array[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    return sum_value - 2 * dp[l][int(half_sum_value)]



print(func([6,7,3,8,2]))