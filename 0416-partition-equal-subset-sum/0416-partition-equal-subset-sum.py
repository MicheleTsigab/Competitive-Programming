class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum= sum(nums)
        if total_sum % 2:
            return False
        half = total_sum //2 
        dp = [False]*(half+1)
        dp[0]=True #not chosing all will result in zero sum
        
        for n in nums:
            for j in range(half,n-1,-1):
                dp[j] = dp[j] or dp[j-n]
        return dp[half]