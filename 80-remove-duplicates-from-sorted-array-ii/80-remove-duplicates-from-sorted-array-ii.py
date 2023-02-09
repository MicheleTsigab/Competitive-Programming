class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
            0,0,1,1,1,1,2,3,3 #check if nums[s-2]==nums[f] we don't move the slow
                s
                f
            prev = - 1
        """
        
        slow = 2
        for fast in range(2,len(nums)):
            if nums[slow-2]!=nums[fast]:
                nums[slow] = nums[fast]
                slow +=1
        return slow                
                    
                