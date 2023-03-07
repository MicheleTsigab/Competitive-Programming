class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
         > < >  < > < > <
        9 4 2 10 7 8 8 1 9
        0 1 0 0 0 0 0 1 1
        
         < > <  > < > < >
        9 4 2 10 7 8 8 1 9
        0 0 1 1  1 1 0 0 0
        """
        even_gt = [0] * len(arr)
        odd_gt = [0] * len(arr)
        
        for i in range(1, len(arr)):
            if i%2!=0 and arr[i] > arr[i-1]:
                odd_gt[i] = 1
            if i%2==0 and arr[i] < arr[i-1]:
                odd_gt[i] = 1
            if i%2==0 and arr[i] > arr[i-1]:
                even_gt[i] = 1
            if i%2!=0 and arr[i] < arr[i-1]:
                even_gt[i] = 1
        max1= self.findMaxConsecutiveOnes(even_gt)
        max2 = self.findMaxConsecutiveOnes(odd_gt)
        return max(max1,max2) + 1    
    def findMaxConsecutiveOnes(self, nums):
        cur_max, gl_max = 0, 0
        for i in nums:
            if i == 1:
                cur_max += 1
                gl_max = max(gl_max, cur_max)
            else:
                cur_max = 0    
        return gl_max