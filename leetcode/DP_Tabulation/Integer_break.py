class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [0] * (n + 1)

        dp[1] = 1

        for num in range(2, n + 1):

            best_product = 0

            for i in range(1, num):

                take_without_breaking = i * (num - i)
                take_and_break = i * dp[num - i]

                best_product = max(
                    best_product,
                    take_without_breaking,
                    take_and_break
                )

            dp[num] = best_product

        return dp[n]