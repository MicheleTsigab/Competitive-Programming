class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j]==nums[j-1]:
                    continue
                values = [nums[i],nums[j]]
                temp=self.twosum(nums,values,target,j+1,n-1)
                res+=temp
        return res
    
    def twosum(self,arr,values,target,l,r):
        if l==len(arr) or r==len(arr):
            return []
        res=[]
        target = target - sum(values)
        while l<r:
            if arr[l]+arr[r]==target:
                res.append([arr[l],arr[r],values[0],values[1]])
                l+=1
                while arr[l]==arr[l-1] and l<r: 
                    l+=1
            elif arr[l]+arr[r]>target:
                r-=1
            else:
                l+=1
        return res