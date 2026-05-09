'''You are given an m x n integer matrix grid, and three integers x, y, and k.

The integers x and y represent the row and column indices of the top-left corner of a square submatrix and the integer k represents the size (side length) of the square submatrix.

Your task is to flip the submatrix by reversing the order of its rows vertically.

Return the updated matrix.'''

class Solution:
    def reverseSubmatrix(self,grid: List[List[int]],x: int,y: int,k: int) -> List[List[int]]:

        # Starting and ending row of submatrix
        top_row = x
        bottom_row = x + k - 1

        # Reverse rows inside submatrix
        while top_row < bottom_row:

            # Swap each column element
            for col in range(y, y + k):
                grid[top_row][col], grid[bottom_row][col] = (
                    grid[bottom_row][col],
                    grid[top_row][col]
                )

            # Move inward
            top_row += 1
            bottom_row -= 1

        return grid
