class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-1,0,-1):
            left= bisect_left(nums, lower - nums[i])
            right = bisect_right(nums,upper - nums[i])
            right-=1
            right = min(right,i-1)
            
            if right - left >=0:
                count += right - left + 1
        return count