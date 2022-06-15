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