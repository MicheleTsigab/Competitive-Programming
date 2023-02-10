class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        right = len(nums) - 1
        count = 0
        mod = (10**9 + 7)
        for left in range(len(nums)):
            while left <= right and nums[left] + nums[right] > target:
                right-=1
            if left <= right and nums[left] + nums[right] <= target:
                count += 1<<(right-left)
                count %= mod
        return count