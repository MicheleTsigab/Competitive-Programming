class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        
        total = sum(nums)
        target = total // k
        #print(nums, target)
        used = [False] * len(nums)
        if total % k or nums[0] > target or (nums[0] < target and nums[0] + nums[-1] > target):
            #print('here')
            return False
        def search(i,k,subsetsum):
            if k==0:
                return True
            if subsetsum == target:
                return search(0,k-1,0) # search number for the other remaining subsets
            for place in range(i,len(nums)):
                if used[place] or subsetsum + nums[place] > target:
                    continue
                used[place]=True
                if search(place+1,k,subsetsum + nums[place]):
                    return True
                used[place]=False
            return False
        return nums[0] <= target and search(0,k,0)
            