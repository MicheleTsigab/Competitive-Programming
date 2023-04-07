class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l=0
        # r=len(nums)-1
        # result=self.bisect(nums,l,r,target)
        result=self.bisect2(nums,target)
        return result
        
    def bisect(self,nums,l,r,target):
        if r>=l:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                l=mid+1
                return self.bisect(nums,l,r,target)
            elif target<nums[mid]:
                r=mid-1
                return self.bisect(nums,l,r,target)
        else:
            return -1
    def bisect2(self,nums,target):
        l=0
        r=len(nums)-1
        while(r>=l):
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                l=mid+1
            elif target<nums[mid]:
                r=mid-1
        return -1
        
           