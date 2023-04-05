class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        def possible(mid):
            
            x = nums.copy()
            
            for i in range(len(x)-1,0,-1):
                if x[i] > mid:
                    change = x[i] - mid
                    x[i] -= change
                    x[i-1] += change
            return max(x)<=mid
        l = 1
        r = max(nums)
        
        ans = r
        while l <= r:
            mid = l + (r-l)//2
            if possible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans