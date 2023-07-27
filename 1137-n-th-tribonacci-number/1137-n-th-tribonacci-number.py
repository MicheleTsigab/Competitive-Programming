class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {0:0,1:1,2:1}
        def compute(n):
            if n in dp:
                return dp[n]
            dp[n] = compute(n-1) + compute(n-2) + compute(n-3)
            return dp[n]
        return compute(n)