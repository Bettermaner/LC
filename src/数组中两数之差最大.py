# 解题思路
    # 如果是一个数字减去它右边子数组中的一个数字可以得到一个差值，则维护一个最大值，因为是左边减去右边
    # 动态规划
    # i表示当前总共几个数的情况下
    # dp[i] = max(dp[i-1] ,(max(array[:i]) - array[i]) ),i 需要从2开始，才能有差值
    # dp[2] = array[0] - array[1] 


    # 我们用变量dif来记录前i+1个数组成的序列的最大数对差。
    # 用变量max来记录前i+1个数的最大值。
    # 那么对于i+1来说，dif=两者最大值{dif，max-a[i+1]}
    # 迭代到最后，dif就储存了最大的数对之差。


    # 如果是一个数字减去它左边子数组中的一个数字可以得到一个差值，则维护一个最小值，因为是右边减去左边
    # dp[i] = max(dp[i-1] ,(array[i] - min(array[:i])) ),i 需要从2开始，才能有差值
    # dp[2] = array[1] - array[0] 
    
# dp[i] # i表示当前总共几个数的情况下右边减去左边的最大差值
def func(array):

    n = len(array)

    dp = [0 for i in range(n+1)]

    dp[2] = array[1] - array[0]

    for i  in range(3,n+1):
        dp[i] = max(dp[i-1] ,array[i-1] - min(array[:i-1]))

    return dp[n]

print(func([4,6,5,8]))
