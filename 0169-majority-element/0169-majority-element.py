class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        def helper(l,r):
            if l==r:
                return nums[l]
            mid = (l + r)//2
            left = helper(l,mid)
            right = helper(mid+1,r)
            if left == right:
                return left
            left_cnt = self.count(nums,left,l,mid)
            right_cnt = self.count(nums,right,mid+1,r)
            if left_cnt > right_cnt:
                return left
            return right
        return helper(0,len(nums)-1)
    def count(self,nums,target,left,right):
        count = 0
        for i in range(left,right+1):
            if nums[i] == target:
                count += 1
        return count