class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0,len(arr) - k
        while l<r:
            mid =l + (r-l)//2
            if x - arr[mid] > arr[mid+k] - x:
                l=mid + 1
            else:
                r=mid
        return arr[l:l+k]