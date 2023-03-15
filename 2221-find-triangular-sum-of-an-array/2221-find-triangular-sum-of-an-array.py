class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        new = []
        for i in range(1,len(nums)):
            new.append((nums[i] + nums[i-1])%10)
      #  print(new)
        return self.triangularSum(new)