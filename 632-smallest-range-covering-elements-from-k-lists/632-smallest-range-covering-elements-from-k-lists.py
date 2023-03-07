class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ordered = []
        for group in range(len(nums)):
            lst = nums[group]
            for num in lst:
                ordered.append([num,group])
        ordered.sort()
        
        count = {}
        left = 0
        k = len(nums)
        ans = [-inf,inf]
        for right,lst in enumerate(ordered):
            num,group = lst
            count[group]= count.get(group,0) + 1
            while len(count) >=k:
                num_left = ordered[left][0]
                group_left = ordered[left][1]
                if ans[1] - ans[0] > num - num_left:
                    ans = [num_left,num]
                count[group_left]-=1
                if count[group_left]==0:
                    del count[group_left]
                left +=1
        return ans
            
                