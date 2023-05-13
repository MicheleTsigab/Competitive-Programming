class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        mod = 10**9 + 7
        def search(given):
            if given == 0:
                return 1
            if given < 0:
                return 0
            if dp[given]!=-1:
                return dp[given]
            ans = (search(given-one))%mod
            ans+= search(given-zero)
            ans%=mod
            dp[given] = ans
            return ans
        dp = [-1] * (high+1)
        soln = 0
        for i in range(low,high+1):
            soln+=search(i)
            soln%=mod
        return soln
        