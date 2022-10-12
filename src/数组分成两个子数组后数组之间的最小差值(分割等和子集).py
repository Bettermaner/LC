# 解题思路
    # 动态规划
    # 求两个子数组的和的最小差值，实际就是让每个子数组的和尽量相等，则是求每个子数组的和的值尽量靠近 sum / 2
    # s1 + s2 = sum, s1 - s2 = diff, 则 diff = sum - 2(s2)
    # dp[i][j] : 表示有i个数的情况下，总的和最接近j的数的总和
    # 状态转移方程 
    # if array[i-1] < j, dp[i][j] = max(dp[i-1][j-array[i-1]] + array[i-1],dp[i-1][j])
    #  else dp[i][j] = dp[i-1][j]
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


# 类似于分割等和数据子集
# 给你一个 只包含正整数 的 非空 数组 nums 。
# 请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
 
def func(array):
    l = len(array)
    sum_value = sum(array)

    if sum_value % 2 != 0:
        return False

    half_sum_value = int(sum_value / 2)


    dp = [ [False for j in range(half_sum_value+1)] for i in range(l+ 1) ]
    dp[0][0] = True

    for i in range(1,l+1):

        for j in range(1,half_sum_value + 1):

            if array[i-1] <= j:
                dp[i][j] = dp[i-1][i-array[i-1]] 
            else:
                dp[i][j] = dp[i-1][j]

    return dp[l][half_sum_value]

print(func([1,2,3,5]))