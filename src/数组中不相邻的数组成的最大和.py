# 解题思路
    # 动态规划
    # i表示当前总共几个数的情况下
    # dp[i] = max(dp[i-2] + array[i], dp[i-1] )
    # dp[0] = array[0]


def max_non_adjacent_sum(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # dp[i] 表示考虑前 i 个数字时的最大不相邻和
    dp = [0] * len(nums)
    dp[0] = nums[0]  # 只有一个数字时，最大和就是它本身
    dp[1] = max(nums[0], nums[1])  # 只有两个数字时，取较大的那个

    for i in range(2, len(nums)):
        # 对于每个数字，有两种选择：
        # 1. 不选当前数字，最大和为 dp[i-1]
        # 2. 选当前数字，最大和为 dp[i-2] + nums[i]
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]

# 示例测试
nums = [2, 4, 6, 2, 5]
print(max_non_adjacent_sum(nums))  # 输出：13 (选择 2, 6, 5)