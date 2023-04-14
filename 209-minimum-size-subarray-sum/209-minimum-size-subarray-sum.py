class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre = [0]
        for n in nums:
            pre.append(pre[-1] + n)
        ans = inf
        for right,n in enumerate(pre):
            if n >= target:
                left = bisect_right(pre,n - target,hi = right)
                ans = min(ans, right - left + 1)
                
        return ans if ans!=inf else 0