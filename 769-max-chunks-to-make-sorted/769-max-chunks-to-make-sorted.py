class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        [1,0,2,3,4]
        max = [1,1,2,3,4]
               0 1 2 3 4
        if max == i:
            count += 1
        make sure max of each range is in it place, if so count
        """
        mx = -1
        count = 0
        for i,n in enumerate(arr):
            mx = max(mx, n)
            if mx==i:
                count += 1
        return count
                