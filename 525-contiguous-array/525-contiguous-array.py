class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        longest = 0
        prefix = {0:-1}
        total = 0
        for right, n in enumerate(nums):
            n = 1 if n else -1
            total+=n
           # print(prefix,total,right)
            if total in prefix:
                left = prefix.get(total)
                longest = max(right - left ,longest)
            else:
                prefix[total]=right
        return longest