# Using recursion and dynamic programming

class Solution:
  
    def recur(self, n,dp):
        #base cases
        
        if(n<0):
            return 0
        if(n==0):
            return 1
        
        #memoization
        
        if(dp[n]!=-1):
            return dp[n]
          
        l = self.recur(n-1,dp)
        r = self.recur(n-2,dp)

        dp[n]=l + r
        
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.recur(n,dp)
