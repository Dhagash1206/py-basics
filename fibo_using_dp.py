def fibonacci_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for index in range(2, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2]
    return dp[n]


# memorization 
def fib(n, memo=None):
    """Return the nth Fibonacci number (0-indexed) using memoization."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n < 2:
        result = n
    else:
        result = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = result
    return result


print(fib(10,memo=None))
