class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        for i in range(len(nums)):
            end1 = nums[i]+k
            left = i + 1
            right = len(nums)-1
            while left <= right:
                mid = (left + right)//2
                if end1 in range(nums[mid]-k,nums[mid]+k+1):
                    left = mid + 1
                else:
                    right = mid - 1
            ans = max(left-i, ans)
        return ans
