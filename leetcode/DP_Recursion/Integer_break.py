class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [-1] * (n + 1)

        def maxProduct(num):

            if num == 1:
                return 1

            if dp[num] != -1:
                return dp[num]

            best_product = 0

            for i in range(1, num):

                take_without_breaking = i * (num - i)
                take_and_break = i * maxProduct(num - i)

                best_product = max(
                    best_product,
                    take_without_breaking,
                    take_and_break
                )

            dp[num] = best_product
            return dp[num]

        return maxProduct(n)