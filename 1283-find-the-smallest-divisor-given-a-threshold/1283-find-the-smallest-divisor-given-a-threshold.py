class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def possible(n):
            total = 0
            for i in nums:
                total+= ceil(i/n)
            return True if total <= threshold else False
        l = 1
        r = max(nums)
        
        while l < r:
            mid = l + (r - l)//2
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        return l
    