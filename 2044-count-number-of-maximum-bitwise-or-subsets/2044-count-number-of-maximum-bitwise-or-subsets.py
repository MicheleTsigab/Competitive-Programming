class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        mx = 0
        def search(i,o):
            nonlocal mx
            if i >= len(nums):
                mx = max(mx,o)
                return
            search(i+1,o | nums[i])
            search(i+1,o)
        search(0,0)
        ans = 0
        def search(i,o):
            nonlocal ans
            if i >= len(nums):
                if o == mx:
                    ans+=1
                return
            search(i+1,o | nums[i])
            search(i+1,o)
        search(0,0)
        return ans