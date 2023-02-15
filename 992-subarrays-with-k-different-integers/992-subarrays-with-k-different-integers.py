class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def subarray_atmost(k):
            count = {}
            left = 0
            ans = 0
            for right, n in enumerate(nums):
                count[n] = count.get(n,0) + 1
                while len(count) > k:
                    num = nums[left]
                    count[num]-=1
                    if count[num]==0:
                        del count[num]
                    left +=1
                N = right - left + 1
                ans += N
            return ans
        return subarray_atmost(k) - subarray_atmost(k-1)