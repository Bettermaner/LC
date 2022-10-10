# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 
# 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，
# 那么就当它是一个数字为 1 的气球。

# 求所能获得硬币的最大数量。

# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# 解题思路
    # 动态规划
    # 假设这个区间是个开区间，最左边索引 i，最右边索引 j
    # 我这里说 “开区间” 的意思是，我们只能戳爆 i 和 j 之间的气球，i 和 j 不要戳
    #  
    # DP思路是这样的，就先别管前面是怎么戳的，你只要管这个区间最后一个被戳破的是哪个气球
    # 这最后一个被戳爆的气球就是 k,k是这个区间   最后一个   被戳爆的气球！！！！！

    # 假设 dp[i][j] 表示开区间 (i,j) 内你能拿到的最多金币
    #  
    # 那么这个情况下
    #  
    # 你在 (i,j) 开区间得到的金币可以由 dp[i][k] 和 dp[k][j] 进行转移
    #  
    # 如果你此刻选择戳爆气球 k，那么你得到的金币数量就是：
    # total= dp[i][k] + val[i] * val[k] * val[j] + dp[k][j]

def func(array):

    # 前后各补充一个默认值1
    array = [1] + array
    array = array + [1]

    n = len(array)
    dp = [[0] * n for i in range(n)]

    def range_best(i,j):
        tmp = 0

        for k in range(i+1,j):
            left = dp[i][k] 
            right = dp[k][j]
            v = array[k]
            t = left + array[j] * v * array[i] + right
            if tmp < t:
                tmp = t
        dp[i][j] = tmp

    #对每一个区间长度进行循环
    for distance in range(2,n): #区间长度 #长度从3开始，n从2开始
        #开区间长度会从3一直到len(nums)
        #因为这里取的是range，所以最后一个数字是len(nums)-1

        #对于每一个区间长度，循环区间开头的i
        for i in range(0,n-distance): #i+n = len(nums)-1

            #计算这个区间的最多金币
            range_best(i,i+distance)

    return dp[0][n-1]

print(func([3,1,5,8]))