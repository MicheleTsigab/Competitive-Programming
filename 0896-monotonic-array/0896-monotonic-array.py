class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        fl = True
        fl2 = True
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                fl = False
                break
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                fl2 = False
                break
        return fl or fl2