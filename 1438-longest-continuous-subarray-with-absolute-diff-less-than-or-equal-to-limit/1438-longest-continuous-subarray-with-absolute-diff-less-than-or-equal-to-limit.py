class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left, right = 0, 0
        max_heap, min_heap = [], []
        res = 0

        while right < len(nums):
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))

            while -max_heap[0][0] - min_heap[0][0] > limit:
                if max_heap[0][1] < min_heap[0][1]:
                    left = max(left, max_heap[0][1] + 1)
                    heapq.heappop(max_heap)
                else:
                    left = max(left, min_heap[0][1] + 1)
                    heapq.heappop(min_heap)

            res = max(res, right - left + 1)
            right += 1

        return res

