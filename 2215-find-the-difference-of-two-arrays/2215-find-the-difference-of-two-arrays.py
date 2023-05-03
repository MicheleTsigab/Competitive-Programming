class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)
        
        ans = []
        temp = []
        for i in n1:

            if i not in n2:
                temp.append(i)
        ans.append(temp)
        temp = []
        for i in n2:

            if i not in n1:
                temp.append(i)
        ans.append(temp)
        return ans