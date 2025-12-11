LCS top down approach

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


Using Bottom Up Approach (Faster Time Complexity)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for row in range(len(text2) - 1, -1, -1):
            for col in range(len(text1) - 1, -1, -1):
                sub_val = dp[row + 1][col + 1]

                if text1[col] == text2[row]:
                    dp[row][col] = sub_val + 1
                else:
                    dp[row][col] = max(dp[row][col + 1], dp[row + 1][col])

        return dp[0][0]
