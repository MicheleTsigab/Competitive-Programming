class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def search(tot,i):
            nonlocal target
            if i == len(nums):
                if tot == target:
                    return 1
                return 0
            add = search(tot + nums[i], i+1)
            sub = search(tot - nums[i],i+1)
            return  add + sub
        return search(0,0)