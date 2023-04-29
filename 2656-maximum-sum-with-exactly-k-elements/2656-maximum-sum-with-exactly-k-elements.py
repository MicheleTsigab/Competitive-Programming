class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        return (m+k)*(m+k-1)//2 - (m)*(m-1)//2