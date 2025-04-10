# 一种衡量两个字符串之间的差异性的方法是，计算两个字符串转换时候需要的最少操作，需要的操作越少说明这两个字符串越相似。
#     假设字符串的操作只有三种：

#     插入一个字符；
#     删除一个字符；
#     替换一个字符；

# 解题思路
    # 动态规划
    # 当a[i] = b[j],如果做其他操作只会让情况变坏，所以不需要做任何操作
        # dp[i][j] = dp[i-1][j-1]
    # 当 a[i] != b[j]
        # 将 a[i] 替换到 b字符中的b[j]上，dp[i][j] = dp[i-1][j-1] + 1
        # 将 a字符中的a[i] 删除，dp[i][j] = dp[i-1][j] + 1
        # 将 b[j] 加入到a字符中 a[i]的后面 ， dp[i][j] = dp[i][j-1] + 1

    # dp[i][j] 表示当a为长度为i，b长度为j时的最小操作

def func(a,b):

    m = len(a)
    n = len(b)

    dp = [[ 0 for j in range(n+1)] for i in range(m+1)]

    # 边界条件
    for i in range(m+1):
        dp[i][0] = i
    
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1,m+1):

        for j in range(1,n+1):

            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = min(min(dp[i-1][j] ,dp[i][j-1]),dp[i-1][j-1]) + 1

    return dp[m][n]


print(func('hello','she'))