def fibonacci(n):
    "斐波拉契"
    dp = [0 for i in range(n)]
    dp[0] = 1
    dp[1] = 1
    
    if n <= 2:
        return 1
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]

if __name__ == "__main__":
    print(fibonacci(5))
