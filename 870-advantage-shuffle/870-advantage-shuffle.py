class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        sorted_nums2 = sorted(((num,i) for i,num in enumerate(nums2)),reverse=True) #we need the index
        nums1.sort()
        left, right = 0, len(nums1) - 1
        ans = [0] * len(nums1)
        for num, i in sorted_nums2:
            if nums1[right] > num:
                ans[i]=nums1[right]
                right -=1
            else:
                ans[i]=nums1[left] #if greater than our greatest just give him the least
                left += 1
        return ans