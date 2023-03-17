class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        prefix_xor = {0:1}
        pre = 0
        ans = 0
        for i in nums:
            pre^=i
            temp = prefix_xor.get(pre,0)
            ans +=temp
            prefix_xor[pre] = temp + 1
        return ans