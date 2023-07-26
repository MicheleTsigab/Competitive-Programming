class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        c = max(cost)
        def minc(i):
            nonlocal c
            if i < 0:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = cost[i] + min(minc(i-1),minc(i-2))
            return dp[i]
        minc(len(cost)-1)
        return min(dp[len(cost)-1],dp[len(cost)-2])
            