class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        #first window
        ans = nums[k-1] - nums[0]
        left = 0
        for right in range(k,len(nums)):
            max_num = nums[right]
            left+=1
            min_num = nums[left]
            ans = min(ans, (max_num - min_num))
        return ans