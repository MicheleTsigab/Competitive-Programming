class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        left, right = 0, 0
        max_deque, min_deque = deque(), deque()
        res = 0

        while right < len(nums):
            while max_deque and nums[right] > max_deque[-1]:
                max_deque.pop()
            while min_deque and nums[right] < min_deque[-1]:
                min_deque.pop()
            max_deque.append(nums[right])
            min_deque.append(nums[right])

            while max_deque and min_deque and max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1

            res = max(res, right - left + 1)
            right += 1

        return res

