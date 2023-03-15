class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]
        # new = []
        # for i in range(1,len(nums)):
        #     new.append((nums[i] + nums[i-1])%10)
        # return self.triangularSum(new)
        r = len(nums) - 1
        while r > 0:
            for i in range(1,r+1):
                nums[i-1] = (nums[i-1] + nums[i]) % 10
            r-=1
        return nums[0]