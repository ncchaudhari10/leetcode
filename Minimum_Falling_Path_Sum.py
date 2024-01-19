class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Initialize a variable to store the minimum falling path sum
        min_sum = float('inf')
        
        # Initialize a memoization table with infinite values
        dp = [[float('inf')] * len(matrix[0]) for _ in range(len(matrix))]

        # Recursive function to calculate the falling path sum
        def recur(row, col):
            # Base case: If the indices are out of bounds, return infinity
            if row < 0 or col < 0 or col > len(matrix[0]) - 1:
                return float('inf')
            
            # Base case: If at the first row, return the matrix value at the current position
            if row == 0:
                return matrix[row][col]

            # Check if the result is already memoized
            if dp[row][col] != float('inf'):
                return dp[row][col]

            # Calculate the falling path sum by considering three possible moves
            up = matrix[row][col] + recur(row - 1, col)
            left = matrix[row][col] + recur(row - 1, col - 1)
            right = matrix[row][col] + recur(row - 1, col + 1)

            # Update the memoization table with the minimum of the three moves
            dp[row][col] = min(up, left, right)
            return dp[row][col]

        # Iterate through the last row of the matrix to find the minimum falling path sum
        for i in range(len(matrix[0])):
            current_sum = recur(len(matrix) - 1, len(matrix[0]) - 1 - i)
            min_sum = min(min_sum, current_sum)

        return min_sum
