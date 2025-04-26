def max_profit(prices):
    "股票买入卖出的最大利润"
    #假设你有一个数组prices，长度为n，其中prices[i]是股票在第i天的价格，请根据这个价格数组，返回买卖股票能获得的最大收益
    # 1.你可以买入一次股票和卖出一次股票，并非每天都可以买入或卖出一次，总共只能买入和卖出一次，且买入必须在卖出的前面的某一天
    #2.如果不能获取到任何利润，请返回0

    #解题思路 动态规划
    # dp[i][j] i表示第几天，j为0或1，0表示未持股 1表示持股
    # 初始状态 dp[0][0] = 0,第0天未持股，收益为0，第0天持股，收益为 -prices[0]
    # 状态转移方程
        # dp[i][0] 当第i天未持股说明有两种情况，1.i-1天也没有持股所以收益与i-1天一样  2.i-1天持股但是在i天卖掉了
        # 因此 dp[i][0] = max(dp[i-1][0],prices[i]-prices[i-1])
        # dp[i][1] 当第i天持股说明有两种情况，1. i-1天也持股，所以收益和i-1天一样  2.i-1天未持股但是第i天买入后持股了
        # 因此 dp[i][1] = max(dp[i-1][1],-prices[i])

    l = len(prices)
    if not l :
        return 0

    dp = [[0,0] for i in range(l)]

    dp[0][0] = 0
    dp[0][1] = -prices[0]

    for day in range(1,l):
        dp[day][0] = max(dp[day-1][0],prices[day] + dp[day-1][1])
        dp[day][1] = max(dp[day-1][1],-prices[day])

    return dp[l-1][0]

# 此方法同样使用于，股票可以多次买入卖出的情况。


# 2.最佳买卖股票时机含冷冻期
# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 输入: prices = [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

#解题思路 动态规划
# dp[i][j] 表示第几天后的最大收益
    # dp[i][0] 表示 第i天持股时，最大收益
    # dp[i][1] 表示 第i天不持股，但是i+1天会在冷冻期的最大收益
    # dp[i][2] 表示 第i天不持股，i+1天也不在冷冻期的最大收益

    # dp[i][0] = max(dp[i-1][0],dp[i-1][2] - prices[i])
    # dp[i][1] = dp[i-1][0] + prices[i]
    # dp[i][2] = max(dp[i-1][2] , dp[i-i][1])

    # n天的最大收益 = max(dp[n-1][1],dp[n-1][2])
    # 边界条件，dp[0][0] = -prices[0], dp[0][1] = 0, dp[0][2] = 0


def func(prices):

    if not prices:
        return 0

    n = len(prices)

    dp = [[-prices[0],0,0]] + [[0,0,0]for i in  range(n)]

    for i in range(1,n):
        dp[i][0]  = max(dp[i-1][0],dp[i-1][2] - prices[i])
        dp[i][1] = dp[i-1][0] + prices[i]
        dp[i][2] = max(dp[i-1][2],dp[i-1][1])

    return max(dp[n-1][1],dp[n-1][2])

print(func([1,2,3,0,2]))



# 3.最佳买卖股票时机V2
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售

# 对于hold状态：
## 如果我们在今天买入股票，则今天的最大利润为not_hold - prices[i]（即前一天不持有股票的利润减去今天的股价）。
## 如果我们继续持有昨天的股票，则今天的最大利润为hold（即昨天持有的利润）。
## 因此，hold = max(hold, not_hold - prices[i])。

#对于not_hold状态：
## 如果我们在今天卖出股票，则今天的最大利润为hold + prices[i]（即昨天持有股票的利润加上今天的股价）。
## 如果我们继续保持不持有股票，则今天的最大利润为not_hold（即昨天不持有股票的利润）。
## 因此，not_hold = max(not_hold, hold + prices[i])。
from typing import List

def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    
    # 初始化状态
    hold, not_hold = -prices[0], 0
    
    for i in range(1, len(prices)):
        # 更新hold和not_hold
        hold = max(hold, not_hold - prices[i])
        not_hold = max(not_hold, hold + prices[i])
    
    # 最终结果是不持有股票时的最大利润
    return not_hold

# 示例
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # 输出应该是7 (买入->1, 卖出->5, 再买入->3, 再卖出->6)