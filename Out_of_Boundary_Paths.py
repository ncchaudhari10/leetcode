import numpy as np
class Solution:
    def recur(self, m, n, maxMove, i, j, dp):
        # Base case: ball crosses the grid boundary
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1

        # Base case: maximum moves exhausted
        if maxMove <= 0:
            return 0

        # Check if result is already memoized
        if dp[i, j, maxMove] != -1:
            return dp[i, j, maxMove]

        # Recursive calls for all possible moves
        up = self.recur(m, n, maxMove - 1, i - 1, j, dp)
        down = self.recur(m, n, maxMove - 1, i + 1, j, dp)
        left = self.recur(m, n, maxMove - 1, i, j - 1, dp)
        right = self.recur(m, n, maxMove - 1, i, j + 1, dp)

        # Memoize the result and return
        dp[i, j, maxMove] = (up + down + left + right) % (10**9 + 7)
        return dp[i, j, maxMove]

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Initialize the memoization array
        dp = np.full((m, n, maxMove + 1), -1, int)

        # Call the recursive function
        return self.recur(m, n, maxMove, startRow, startColumn, dp)
