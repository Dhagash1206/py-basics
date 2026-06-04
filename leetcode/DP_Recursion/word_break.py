class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                nw = len(w)
                if (i + nw) <= n and s[i:i + nw] == w:
                    dp[i] = dp[i + nw]

                if dp[i]:
                    break

        return dp[0]
