class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ans = -1
        nums.sort()
        tot = nums[0] + nums[1]
        for i in range(2,len(nums)):
            
            if tot > nums[i]:
                ans = tot + nums[i]
            tot += nums[i]
        return ans
                