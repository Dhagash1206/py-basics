class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def solve(remaining: int) -> int:
            if remaining == 0:
                return 0

            if dp[remaining] != -1:
                return dp[remaining]

            answer = float("inf")

            sq_r = 1
            
            while sq_r * sq_r <= remaining:
                perfect_square = sq_r * sq_r
                answer = min(answer,1 + solve(remaining - perfect_square))
                sq_r += 1

            dp[remaining] = answer
            return answer

        return solve(n)