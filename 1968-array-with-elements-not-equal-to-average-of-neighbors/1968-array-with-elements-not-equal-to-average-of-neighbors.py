class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # result=[0]*len(nums)
        # mid=len(nums)//2 if len(nums)%2 else len(nums)//2-1
        # odd=1
        # even=0
        # for idx,i in enumerate(nums):
        #     if mid>=0:
        #         result[even]=i
        #         even+=2
        #         mid-=1
        #     else:
        #         result[odd]=i
        #         odd+=2
        # return result
        # nums.sort()
        # for i in range(1,len(nums),2):
        #     nums[i],nums[i-1]=nums[i-1],nums[i]
        # return nums
        res=[]
        nums.sort()
        left = 0
        right =len(nums) -1
        while left < right:
            res.append(nums[left])
            res.append(nums[right])
            right-=1
            left+=1
        if len(res)<len(nums):
            res.append(nums[left])
        return res