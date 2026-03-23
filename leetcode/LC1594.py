# 1594. Maximum Non Negative Product in a Matrix

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        rows, cols = len(grid), len(grid[0])

        # dp_max[i][j] → max product till (i, j)
        # dp_min[i][j] → min product till (i, j)
        dp_max = [[0] * cols for _ in range(rows)]
        dp_min = [[0] * cols for _ in range(rows)]

        dp_max[0][0] = dp_min[0][0] = grid[0][0]

        # First row
        for j in range(1, cols):
            val = grid[0][j]
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j - 1] * val

        # First column
        for i in range(1, rows):
            val = grid[i][0]
            dp_max[i][0] = dp_min[i][0] = dp_max[i - 1][0] * val

        # Fill rest of grid
        for i in range(1, rows):
            for j in range(1, cols):
                val = grid[i][j]

                top_max, top_min = dp_max[i - 1][j], dp_min[i - 1][j]
                left_max, left_min = dp_max[i][j - 1], dp_min[i][j - 1]

                if val >= 0:
                    dp_max[i][j] = max(top_max, left_max) * val
                    dp_min[i][j] = min(top_min, left_min) * val
                else:
                    dp_max[i][j] = min(top_min, left_min) * val
                    dp_min[i][j] = max(top_max, left_max) * val

        result = dp_max[rows - 1][cols - 1]

        return result % MOD if result >= 0 else -1