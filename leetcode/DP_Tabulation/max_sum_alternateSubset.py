# Maximum Sum of Subsequence With Non-adjacent Elements

def maxsum_arr_nonadjacent(arr):

    n = len(arr)

    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    dp = n * [0]

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

    return dp[n - 1]


arr = [2,3,5,7,8,1,3]
print(maxsum_arr_nonadjacent(arr))