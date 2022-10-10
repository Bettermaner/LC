# 解题思路
    # 动态规划
    # 假设i表示需要兑换的金额， 有j种零钱，每种零钱个数无上限
    # 转移方程：dp[i] = min(dp[i - coin[0]] + 1,dp[i -coin[1] + 1, .....,dp[i-coin[j] + 1]]
    # 初始值： dp[0] = 0


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # dp[i] 表示凑出 i 所需的最少硬币数量，
        # 初始化为 amount + 1 ，表示当前还凑不出
        dp = [amount + 1] * (amount + 1)
        # 最开始只能确认不需要任何硬币就可以凑出 0
        dp[0] = 0
        # 遍历要凑的数字状态
        for i in range(1, amount + 1):
            # 遍历当前选择的硬币
            for coin in coins:
                # 如果 i >= coin 时，
                # 则可以选择 coin ，进行状态转移
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == amount + 1:
            # 无法凑出 amount ，返回 -1
            return -1

        # dp[amount] 就是所需的最少硬币数量
        return dp[amount]