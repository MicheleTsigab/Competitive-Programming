class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
         0 1 2 3 4  5 6
        [5,7,7,8,8,10] t =11
               l
               m
        flag = True
        l =0 , 3
         r = 5, 3
         mid = 2, 4, 2  
         O(log(n))
         2 binary searches over the original 
         """
        l = bisect_left(nums,target)
        r = bisect_right(nums,target) - 1
        if l>=len(nums) or nums[l]!=target:
            return [-1,-1]
        return [l,r]