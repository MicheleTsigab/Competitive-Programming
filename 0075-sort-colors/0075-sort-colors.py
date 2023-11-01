class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
            r
        0 0 1 1 2 2
              b w
        """
        #nice soln one pass
        red = 0 #left pointer represent 0
        white = 0 #medium pointer rep 1
        blue = len(nums)-1 #last pointer 2
        
        while white<=blue:
            if nums[white]==0:
                nums[white],nums[red] = nums[red],nums[white]
                white +=1
                red +=1
            elif nums[white]==1: #skip one place
                white +=1
            else: #2 occured
                nums[white],nums[blue] = nums[blue], nums[white]
                blue -=1
        
        #counting sort
        # count=[0]*3
        # for i in nums:
        #     count[i]+=1
        # pointer =0
        # for n in range(3):
        #     freq=count[n]
        #     for f in range(freq):
        #         nums[pointer]=n
        #         pointer+=1