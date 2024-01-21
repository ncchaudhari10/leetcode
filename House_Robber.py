class Solution:
    def recur(self, i, nums, dp):
        # Base case: If i is greater than or equal to the length of nums, no more houses to rob.
        if i >= len(nums):
            return 0

        # If the result for this index is already memoized, return it.
        if dp[i] != -1:
            return dp[i]

        # Rob the current house (i) and move to the house two steps ahead (i+2)
        l = self.recur(i + 2, nums, dp) + nums[i]

        # Skip the current house and move to the next one (i+1)
        r = self.recur(i + 1, nums, dp)

        # Save the maximum result in the memoization table
        dp[i] = max(l, r)

        # Return the maximum result for the current house
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        # Initialize a memoization table with -1 for each house
        dp = [-1] * len(nums)
        
        # Start the recursive function from the first house
        return self.recur(0, nums, dp)
