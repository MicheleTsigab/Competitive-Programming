class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        
        for s in range(len(nums)):
            if nums[s]:
                nums[s],nums[p] = nums[p],nums[s]
                p +=1