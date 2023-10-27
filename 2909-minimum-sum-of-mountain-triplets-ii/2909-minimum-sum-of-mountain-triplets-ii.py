class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minimum_left = []
        n = len(nums)
        for i in range(0,len(nums)):
            if not minimum_left:
                minimum_left.append(nums[0])
                continue
            minimum_left.append(min(minimum_left[-1],nums[i-1]))
        minimum_right = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                minimum_right[i]=nums[i]
                continue
            minimum_right[i] = min(nums[i+1],minimum_right[i+1])
        ans = inf
        #print(minimum_left,minimum_right)
        for j in range(0,n):
            pos_i = inf
            if minimum_left[j] >= nums[j] or minimum_right[j] >= nums[j]:
                continue
            ans = min(ans, nums[j] + minimum_left[j] + minimum_right[j])
        return -1 if ans == inf else ans