class Solution:
    def lenLongestFibSubseq(self, arr):
        n = len(arr)
        index = {x: i for i, x in enumerate(arr)}
        dp = [[2] * n for _ in range(n)]
        ans = 0

        for k in range(n):
            for j in range(k):
                prev = arr[k] - arr[j]
                if prev < arr[j] and prev in index:
                    i = index[prev]
                    dp[j][k] = dp[i][j] + 1
                    ans = max(ans, dp[j][k])

        return ans if ans >= 3 else 0