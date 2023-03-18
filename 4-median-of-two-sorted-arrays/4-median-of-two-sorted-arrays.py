class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
         0 1    0 1
        [1,2], [3,4]
         l r
         m = 0
         half = 2
         2 - m - 2
         
        """
        
        n = len(nums1) + len(nums2)
        half = n//2 #floor 
        odd = True if n%2!=0 else False
        if len(nums2) < len(nums1):
            nums1,nums2 = nums2,nums1
            
        l = 0
        r = len(nums1) - 1
        while True:
            mid = l + (r- l)//2
            p2 = half - mid - 2 #get index of the second partition
            first = nums1[mid] if mid >=0 else -math.inf
            first_next = nums1[mid + 1] if (mid + 1) < len(nums1) else math.inf
            second = nums2[p2] if p2 >= 0 else -math.inf
            second_next = nums2[p2 + 1] if (p2 + 1) < len(nums2) else math.inf
            if first <= second_next and second <= first_next:
                mn = min(second_next,first_next)
                if odd:
                    return mn
                return (max(first,second) + mn)/2
            elif first > second_next:
                r = mid - 1
            elif second > first_next:
                l = mid + 1