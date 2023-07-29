class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = {0:0,1:1}
        if n ==0:
            return 0
        def compute(i):
            nonlocal n
            if 2*i + 1 > n:
                return
            dp[2*i] = dp[i]
            dp[2*i+1] = dp[i] + dp[i+1]
            compute(i+1)
                
        compute(1)
        return max(dp.items(),key = lambda a:a[1])[1]