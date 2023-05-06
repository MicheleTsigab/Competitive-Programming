class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        ans = 0
        mod = 10**9 + 7
        for i in range(len(nums)):
            r = bisect_right(nums,target - nums[i])-1 
            if r >= i:
                ans += pow(2,r-i,mod)
        return ans % mod