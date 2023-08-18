class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        nums = sorted([v,i] for i,v in enumerate(nums))
        min_hp1 = []
        min_hp2 = []
        res = inf
        for val,idx in nums:
            heappush(min_hp1,[x + idx,val])
            heappush(min_hp2,[x - idx,val])
            
            while min_hp1 and min_hp1[0][0] <= idx:
                res = min(res,abs(val - heappop(min_hp1)[1]))
            while min_hp2 and min_hp2[0][0] <= -idx:
                res = min(res,abs(val - heappop(min_hp2)[1]))
        return res