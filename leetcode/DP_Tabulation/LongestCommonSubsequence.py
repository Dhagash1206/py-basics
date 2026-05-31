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
