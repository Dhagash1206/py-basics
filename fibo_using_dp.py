def fibonacci_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for index in range(2, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2]
    return dp[n]
