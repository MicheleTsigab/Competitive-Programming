class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        longest = 0
        prefix = {0:0}
        total = 0
        for right, n in enumerate(nums):
            n = 1 if n else -1
            total+=n
           # print(prefix,total,right)
            if total in prefix:
                left = prefix.get(total)
                longest = max(right - left + 1 ,longest)
            else:
                prefix[total]=right + 1
        return longest