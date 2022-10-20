# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

# 解题思路
    # 动态规划
    # Xn+1 = Xa * 2, Xb * 3, Xc * 5 , a in [1:n],b in [1:n],c in [1:n]
    # 由于 Xn+1 是 最接近 Xn的丑数，因此索引 a, b, c 需满足以下条件：
        # Xa * 2 > Xn >= Xa-1 * 2
        # Xb * 3 > Xn >= Xb-1 * 3
        # Xc * 5 > Xn >= Xc-1 * 5

    # dp[i] 表示第i+1个丑数,dp[0] = 1


def func(n):
    dp = [1] * n

    a,b ,c = 0,0,0

    for i in  range(1,n):
        a_v,b_v,c_v = dp[a] * 2,dp[b] * 3, dp[c] * 5 
        v = min(a_v,b_v,c_v)
        dp[i] = v
        if v == a_v:
            a += 1
        if v == b_v:
            b += 1
        if v == c_v:
            c += 1

    return dp[n-1]

print(func(10))