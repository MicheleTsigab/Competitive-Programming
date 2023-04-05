class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r-l)//2
            left_num = nums[mid - 1] if mid - 1 >= 0 else -inf
            right_num = nums[mid + 1] if mid + 1 < len(nums) else -inf
            
            if nums[mid] > left_num and nums[mid] > right_num:
                return mid
            if nums[mid] < left_num:
                r = mid - 1
            else:
                l = mid + 1
        
            