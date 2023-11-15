class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        for i in range(len(nums)):
            end1 = nums[i]+k
            left = i + 1
            right = len(nums)-1
            found = i
            while left <= right:
                mid = (left + right)//2

                if end1 in range(nums[mid]-k,nums[mid]+k+1):

                    found = mid
                    left = mid + 1
                else:
                    right = mid - 1
            ans = max(found-i+1, ans)
        return ans
