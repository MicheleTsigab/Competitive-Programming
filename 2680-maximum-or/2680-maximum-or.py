class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        x = 0
        pre = [0]
        suf = []
        for i in nums:
            pre.append(pre[-1]|i)
        for i in reversed(nums):
            if not suf:
                suf.append(i)
                continue
            suf.append(suf[-1]|i)
        suf.reverse()
        suf.append(0)
        res = 0
        m = 1<<k
        
        for i in range(len(nums)):
            temp = pre[i] | suf[i+1]
            res= max(res, (m * nums[i])|temp)
                
        return res