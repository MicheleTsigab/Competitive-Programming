class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def search(i,o):
            if i >= len(nums):
                return o
            return max(search(i+1,o | nums[i]),search(i+1,o))
        mx = search(0,0)
        ans = 0
        @lru_cache(None)
        def search(i,o):
            nonlocal mx
            if i >= len(nums):
                if mx == o:
                    return 1
                else:
                    return 0
            return search(i+1,o | nums[i]) + search(i+1,o)
        
        return search(0,0)
