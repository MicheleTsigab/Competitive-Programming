class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:        
    
        """
        [2,1,4,3] 
        1
        [2,1]
       
        """
        def atmost(bound):
            ans, left = 0,0
            for right,n in enumerate(nums):
                if n > bound:
                    left = right + 1
                    continue
                ans+= (right - left + 1)
            return ans
            
        return atmost(right) - atmost(left - 1)