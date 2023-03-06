class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        total = 0
        #first window
        for i in range(k):
            total +=nums[i]
        
        ans = total / k
        left = 0
        for right in range(k, len(nums)):
            total += nums[right] - nums[left]
            left +=1
            ans = max(total / k, ans)
        return ans