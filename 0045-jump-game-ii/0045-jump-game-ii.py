class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [inf] * len(nums)
        dp[0] = 0
        for i,n in enumerate(nums):
            for j in range(i,min(i+n+1,len(nums))):
                    dp[j] = min(dp[j], dp[i] + 1)
       # print(dp)
        return dp[-1]