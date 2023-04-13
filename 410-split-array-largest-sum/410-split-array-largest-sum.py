class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def possible(mid):
            part = k
            total = 0
            for i in nums:
                if total + i <= mid:
                    total+=i
                elif part:
                    part -=1
                    total = 0
                    if total + i > mid:
                        return False 
                    total+=i
            return part > 0
        l = max(nums)
        r = sum(nums)
        ans = r
        while l<=r:
            mid = l + (r-l)//2
            if possible(mid):
                ans = min(ans,mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans