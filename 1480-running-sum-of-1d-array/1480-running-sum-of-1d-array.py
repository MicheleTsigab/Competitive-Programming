class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if not res:
                res.append(i)
                continue
            res.append(res[-1]+i)
        return res