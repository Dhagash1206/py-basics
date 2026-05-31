class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1 = text1
        s2 = text2
        dp = [[-1] * len(s2) for _ in range(len(s1))]

        def LCS(s1, s2, i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i] == s2[j]:
                dp[i][j] = 1 + LCS(s1, s2, i - 1, j - 1)
            else:
                dp[i][j] = max(
                    LCS(s1, s2, i - 1, j),
                    LCS(s1, s2, i, j - 1)
                )
            return dp[i][j]

        return LCS(s1, s2, len(s1) - 1, len(s2) - 1)

