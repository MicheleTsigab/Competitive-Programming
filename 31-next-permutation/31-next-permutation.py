class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1 1 5
          
        

  
        """
        k = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                k = i
                break
        if k==-1: # all numbers are in a descending order hence the cycle is reached
            nums.reverse()
            return
        #greater than k starting from end
        greater = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > nums[k]:
                greater = i
                break
        nums[k],nums[greater] = nums[greater],nums[k]
        
        #reverse to make the elements after k sorted
        right = len(nums) - 1
        k+=1
        while k < right:
            nums[k],nums[right] = nums[right],nums[k]
            k+=1
            right-=1
        
        
        