class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        #we can just make the three elements equal to the last element
        if len(nums) <= 4:
            return 0
        #else 4 possibilities
        #remove 0,1,2 index
        #remove 0,1 and last index
        #remove 0 and last two index
        #remove last three index
        return min(nums[-1] - nums[3],nums[-2] - nums[2],nums[-3]-nums[1],nums[-4]-nums[0])
        