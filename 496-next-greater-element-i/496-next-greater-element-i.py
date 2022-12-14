class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap={i:-1 for i in nums1}
        stack=[]
        
        for i,num in enumerate(nums2):
            while stack and num>stack[-1]:
                temp=stack.pop()
                hashmap[temp]=num
            if num in hashmap:
                stack.append(num)
        return hashmap.values()
        #naive solution o(m*n)
        # for i,num in enumerate(nums2):
        #     temp=-1
        #     if num in hashmap:
        #         for j in range(i,len(nums2)):
        #             if nums2[j]>num:
        #                 temp=nums2[j]
        #                 break
        #         hashmap[num]=temp
        # return hashmap.values()