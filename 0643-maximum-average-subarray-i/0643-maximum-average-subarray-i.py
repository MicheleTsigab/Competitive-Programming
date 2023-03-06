class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        1 2 3 4 5
          l   r
        ave = max(ave,ave(l,r))
        """
        total = 0
        #first window
        for i in range(k):
            total +=nums[i]
        
        ans = total / k
        for right in range(k, len(nums)):
            total += nums[right] - nums[right - k]
            #left +=1
            ans = max(total / k, ans)
        return ans