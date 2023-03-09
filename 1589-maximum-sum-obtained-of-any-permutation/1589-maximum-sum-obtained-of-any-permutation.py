class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        pre = [0] * len(nums)
        
        for l,r in requests:
            pre[l]+=1
            if r+1 < len(nums):
                pre[r+1]-=1
        for i in range(1,len(pre)):
            pre[i]+=pre[i-1]
            
        nums.sort(reverse=True)
        pre.sort(reverse=True)
        result = 0
        for i in range(len(nums)):
            result += nums[i]* pre[i]
            
        return result % (10**9 + 7)