class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        l = 0
        r = 1000
        ans = l
        while l <= r:
            mid = l + (r-l)//2
            x =len(citations) - bisect_left(citations,mid)
            if x >= mid:
                ans = max(ans,mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans