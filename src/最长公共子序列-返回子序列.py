# 比如： a = (3,2,1,4,5) , b= (1,2,3,4,5) 那么二者最大的公共子序列为 (2,4,5)

# 解题思路
## 动态规划
# 时间复杂度	O(m × n)
# 空间复杂度	O(m × n)

def run(x,y):

    m,n = len(x),len(y)

   
    dp = [[0] * (n+1) for i in range(m+1)]
     # dp[0][0]表示x第0个元素，y第0个元素下对应的最大公共子序列长度
    dp[0][0] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    i = n
    j = m
    
    res = []
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j-= 1
    
    return res