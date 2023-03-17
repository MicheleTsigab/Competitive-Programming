class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
         0 1 2 3 4 5
        [5,7,7,8,8,10] t = 8
               l  r
               m
        flag = True
        l =0 , 3
         r = 5, 3
         mid = 2, 4, 2  
         O(log(n))
         2 binary searches over the original 
         """
        l = 0
        r = len(nums) - 1
        flag = False #indicate not found
        #left most
        while l<=r:
            mid = l + (r- l )//2
            if target > nums[mid]:
                l = mid + 1
            else:
                if nums[mid]==target:
                    flag = True
                r = mid - 1
        if not flag:
            return [-1,-1]
        ans = []
        
        ans.append(l)
        #right most
        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = l + (r- l )//2
            if target >= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        ans.append(r)
        return ans