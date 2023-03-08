class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        #print(self.atmostk(nums,k), self.atmostk(nums,k-1))
        return self.atmostk(nums,k) - self.atmostk(nums,k-1)
    def atmostk(self,nums,k):
        odd = 0
        left = 0
        ans = 0
        for right,n in enumerate(nums):
            if n%2!=0:
                odd+=1
            while left <= right and odd > k:
                if nums[left]%2!=0:
                    odd-=1
                left+=1
            ans+=right - left + 1
        return ans