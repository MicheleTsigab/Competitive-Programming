class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre={0:-1}
        sump=0
        for i,n in enumerate(nums):
            sump+=n
            rem = sump % k
            
            if rem not in pre:
                pre[rem] = i
            elif i - pre[rem] > 1:
                return True
        return False